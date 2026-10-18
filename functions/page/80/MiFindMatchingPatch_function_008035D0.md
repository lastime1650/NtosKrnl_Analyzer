# MiFindMatchingPatch

- RVA: `0x008035D0`–`0x00803605` (길이 `53` bytes)
- VA: `0x00000001408035D0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `18`개 명령, `53/53` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008035D0  83 7A 10 00                     cmp dword ptr [rdx + 0x10], 0
008035D4  74 0C                           je 0x1408035e2
008035D6  48 3B 0A                        cmp rcx, qword ptr [rdx]
008035D9  74 22                           je 0x1408035fd
008035DB  B8 01 00 00 00                  mov eax, 1
008035E0  C3                              ret
008035E1  CC                              int3
008035E2  4C 8B 02                        mov r8, qword ptr [rdx]
008035E5  41 8B 40 78                     mov eax, dword ptr [r8 + 0x78]
008035E9  39 41 78                        cmp dword ptr [rcx + 0x78], eax
008035EC  75 ED                           jne 0x1408035db
008035EE  41 8B 80 9C 00 00 00            mov eax, dword ptr [r8 + 0x9c]
008035F5  39 81 9C 00 00 00               cmp dword ptr [rcx + 0x9c], eax
008035FB  75 DE                           jne 0x1408035db
008035FD  48 89 4A 08                     mov qword ptr [rdx + 8], rcx
00803601  33 C0                           xor eax, eax
00803603  C3                              ret
00803604  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiFindMatchingPatch(__int64 a1, __int64 a2)
{
    __int64 result;

    if ((*(unsigned int *)(a2 + 16)) == 0) goto loc_008035E2;
    if (a1 == (*(unsigned __int64 *)(a2))) goto loc_008035FD;
loc_008035DB:
    return 1;
loc_008035E2:
    if ((*(unsigned int *)(a1 + 120)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 120))))) goto loc_008035DB;
    if ((*(unsigned int *)(a1 + 156)) != ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2) + 156))))) goto loc_008035DB;
loc_008035FD:
    *(unsigned __int64 *)(a2 + 8) = a1;
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiFindMatchingPatch(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;

    if ((*(uint32_t *)(arg2 + 0x10)) == 0) goto loc_008035E2;
    if (Arg1 == (*(uint64_t *)(arg2))) goto loc_008035FD;
loc_008035DB:
    return 1;
loc_008035E2:
    if ((*(uint32_t *)(arg1 + 0x78)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x78))))) goto loc_008035DB;
    if ((*(uint32_t *)(arg1 + 0x9C)) != ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2) + 0x9C))))) goto loc_008035DB;
loc_008035FD:
    *(void **)(arg2 + 0x8) = Arg1;
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x78` | `32` | `R` |
| `Arg1` | `+ 0x9C` | `32` | `R` |
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `W` |
| `Arg2` | `+ 0x10` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008035D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008035D0[BB_008035D0]
  bb_008035D6[BB_008035D6]
  bb_008035DB[BB_008035DB]
  bb_008035E1[BB_008035E1]
  bb_008035E2[BB_008035E2]
  bb_008035EE[BB_008035EE]
  bb_008035FD[BB_008035FD]
  bb_00803604[BB_00803604]
  bb_008035D0 -->|branch| bb_008035E2
  bb_008035D0 -->|fallthrough| bb_008035D6
  bb_008035D6 -->|branch| bb_008035FD
  bb_008035D6 -->|fallthrough| bb_008035DB
  bb_008035E1 -->|flow| bb_008035E2
  bb_008035E2 -->|branch| bb_008035DB
  bb_008035E2 -->|fallthrough| bb_008035EE
  bb_008035EE -->|branch| bb_008035DB
  bb_008035EE -->|fallthrough| bb_008035FD
```
