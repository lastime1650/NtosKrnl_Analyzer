# PipEnumeratePersistedMemory

- RVA: `0x00724E80`–`0x00724E9E` (길이 `30` bytes)
- VA: `0x0000000140724E80`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `11`개 명령, `30/30` bytes 표시
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
00724E80  49 8B 08                        mov rcx, qword ptr [r8]
00724E83  48 85 C9                        test rcx, rcx
00724E86  75 06                           jne 0x140724e8e
00724E88  41 FF 40 08                     inc dword ptr [r8 + 8]
00724E8C  EB 0C                           jmp 0x140724e9a
00724E8E  41 8B 40 0C                     mov eax, dword ptr [r8 + 0xc]
00724E92  48 89 14 C1                     mov qword ptr [rcx + rax*8], rdx
00724E96  41 FF 40 0C                     inc dword ptr [r8 + 0xc]
00724E9A  33 C0                           xor eax, eax
00724E9C  C3                              ret
00724E9D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PipEnumeratePersistedMemory(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    if (*(unsigned __int64 *)(a3) != 0) goto loc_00724E8E;
    goto loc_00724E9A;
loc_00724E8E:
    *(unsigned __int64 *)(*(unsigned __int64 *)(a3) + (unsigned int)(*(unsigned int *)(a3 + 12)) * 8) = a2;
loc_00724E9A:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PipEnumeratePersistedMemory(int64_t Arg1, int64_t Arg2, void *Arg3)
{
    uint8_t *arg3 = (uint8_t *)Arg3;

    int64_t result;

    if (*(uint64_t *)(arg3) != 0) goto loc_00724E8E;
    goto loc_00724E9A;
loc_00724E8E:
    *(uint64_t *)(*(uint64_t *)(arg3) + (uint32_t)(*(uint32_t *)(arg3 + 0xC)) * 8) = Arg2;
loc_00724E9A:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg3` | `+ 0x0` | `64` | `R` |
| `Arg3` | `+ 0x8` | `32` | `R/W` |
| `Arg3` | `+ 0xC` | `32` | `R` |
| `Arg3` | `+ 0xC` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00724E80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00724E80[BB_00724E80]
  bb_00724E88[BB_00724E88]
  bb_00724E8E[BB_00724E8E]
  bb_00724E9A[BB_00724E9A]
  bb_00724E9D[BB_00724E9D]
  bb_00724E80 -->|branch| bb_00724E8E
  bb_00724E80 -->|fallthrough| bb_00724E88
  bb_00724E88 -->|branch| bb_00724E9A
  bb_00724E8E -->|flow| bb_00724E9A
```
