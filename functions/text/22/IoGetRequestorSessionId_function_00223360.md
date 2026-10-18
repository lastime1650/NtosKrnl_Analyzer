# IoGetRequestorSessionId

- RVA: `0x00223360`–`0x00223394` (길이 `52` bytes)
- VA: `0x0000000140223360`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005F758`
- 디코드: `15`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0022337A` → [PsGetProcessSessionId](PsGetProcessSessionId_function_002233A0.md) (function, `0x002233A0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00223360  48 83 EC 28                     sub rsp, 0x28
00223364  48 8B 89 98 00 00 00            mov rcx, qword ptr [rcx + 0x98]
0022336B  4C 8B C2                        mov r8, rdx
0022336E  48 85 C9                        test rcx, rcx
00223371  74 17                           je 0x14022338a
00223373  48 8B 89 20 02 00 00            mov rcx, qword ptr [rcx + 0x220]
0022337A  E8 21 00 00 00                  call 0x1402233a0
0022337F  41 89 00                        mov dword ptr [r8], eax
00223382  33 C0                           xor eax, eax
00223384  48 83 C4 28                     add rsp, 0x28
00223388  C3                              ret
00223389  CC                              int3
0022338A  83 0A FF                        or dword ptr [rdx], 0xffffffff
0022338D  B8 01 00 00 C0                  mov eax, 0xc0000001
00223392  EB F0                           jmp 0x140223384
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IoGetRequestorSessionId(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    if (*(unsigned __int64 *)(a1 + 152) == 0) goto loc_0022338A;
    result = PsGetProcessSessionId(*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 152) + 544), a2, a2, a4);
    *(unsigned int *)(a2) = (unsigned int)(result);
    result = 0;
loc_00223384:
    v_rsp = (v_rsp) + (40);
    return result;
loc_0022338A:
    goto loc_00223384;
}
```

## 5. (Beta) C Style

```c
int64_t IoGetRequestorSessionId(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    if (*(uint64_t *)(arg1 + 0x98) == 0) goto loc_0022338A;
    result = PsGetProcessSessionId(*(uint64_t *)(*(uint64_t *)(arg1 + 0x98) + 0x220), Arg2, Arg2, a4);
    *(uint32_t *)(arg2) = (uint32_t)(result);
    result = 0;
loc_00223384:
    local_rsp = (local_rsp) + (40);
    return result;
loc_0022338A:
    goto loc_00223384;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x98` | `64` | `R` |
| `Arg2` | `+ 0x0` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00223360&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00223360[BB_00223360]
  bb_00223373[BB_00223373]
  bb_00223384[BB_00223384]
  bb_00223389[BB_00223389]
  bb_0022338A[BB_0022338A]
  bb_00223360 -->|branch| bb_0022338A
  bb_00223360 -->|fallthrough| bb_00223373
  bb_00223373 -->|flow| bb_00223384
  bb_00223389 -->|flow| bb_0022338A
  bb_0022338A -->|branch| bb_00223384
```
