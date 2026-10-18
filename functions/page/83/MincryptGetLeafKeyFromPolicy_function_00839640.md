# MincryptGetLeafKeyFromPolicy

- RVA: `0x00839640`–`0x00839667` (길이 `39` bytes)
- VA: `0x0000000140839640`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `15`개 명령, `39/39` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SecureDump_ValidateAmeCertChain](../../text/5A/SecureDump_ValidateAmeCertChain_function_005A38B0.md) at `0x005A3962`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00839640  83 39 00                        cmp dword ptr [rcx], 0
00839643  74 1E                           je 0x140839663
00839645  48 8B 41 10                     mov rax, qword ptr [rcx + 0x10]
00839649  48 85 C0                        test rax, rax
0083964C  74 15                           je 0x140839663
0083964E  F7 41 08 00 00 FF FF            test dword ptr [rcx + 8], 0xffff0000
00839655  75 0C                           jne 0x140839663
00839657  83 78 10 00                     cmp dword ptr [rax + 0x10], 0
0083965B  74 06                           je 0x140839663
0083965D  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00839661  C3                              ret
00839662  CC                              int3
00839663  33 C0                           xor eax, eax
00839665  C3                              ret
00839666  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MincryptGetLeafKeyFromPolicy(__int64 a1)
{
    __int64 result;

    if ((*(unsigned int *)(a1)) == 0) goto loc_00839663;
    if (*(unsigned __int64 *)(a1 + 16) == 0) goto loc_00839663;
    if (((*(unsigned int *)(a1 + 8)) & (0xFFFF0000ULL)) != 0) goto loc_00839663;
    if ((*(unsigned int *)(*(unsigned __int64 *)(a1 + 16) + 16)) == 0) goto loc_00839663;
    return *(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 16) + 8);
loc_00839663:
    result = 0;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MincryptGetLeafKeyFromPolicy(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if ((*(uint32_t *)(arg1)) == 0) goto loc_00839663;
    if (*(uint64_t *)(arg1 + 0x10) == 0) goto loc_00839663;
    if (((*(uint32_t *)(arg1 + 0x8)) & (0xFFFF0000ULL)) != 0) goto loc_00839663;
    if ((*(uint32_t *)(*(uint64_t *)(arg1 + 0x10) + 0x10)) == 0) goto loc_00839663;
    return *(uint64_t *)(*(uint64_t *)(arg1 + 0x10) + 0x8);
loc_00839663:
    result = 0;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00839640&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00839640[BB_00839640]
  bb_00839645[BB_00839645]
  bb_0083964E[BB_0083964E]
  bb_00839657[BB_00839657]
  bb_0083965D[BB_0083965D]
  bb_00839662[BB_00839662]
  bb_00839663[BB_00839663]
  bb_00839666[BB_00839666]
  bb_00839640 -->|branch| bb_00839663
  bb_00839640 -->|fallthrough| bb_00839645
  bb_00839645 -->|branch| bb_00839663
  bb_00839645 -->|fallthrough| bb_0083964E
  bb_0083964E -->|branch| bb_00839663
  bb_0083964E -->|fallthrough| bb_00839657
  bb_00839657 -->|branch| bb_00839663
  bb_00839657 -->|fallthrough| bb_0083965D
  bb_00839662 -->|flow| bb_00839663
```
