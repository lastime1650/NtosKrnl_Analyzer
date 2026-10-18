# EtwTimLogProhibitFsctlSystemCalls

- RVA: `0x00A81E18`–`0x00A81E65` (길이 `77` bytes)
- VA: `0x0000000140A81E18`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B71CC`
- 디코드: `21`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x00A81E56` → [EtwpTimLogMitigationForProcess](EtwpTimLogMitigationForProcess_function_00A81E6C.md) (function, `0x00A81E6C`)

### Direct callers
- [IopXxxControlFile](../8E/IopXxxControlFile_function_008E9AD0.md) at `0x008EAB09`

### Static image references
- `0x00A81E3A` → RVA `0x0001BC98` (`.rdata`; read)
- `0x00A81E43` → RVA `0x0001BC88` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A81E18  40 53                           push rbx
00A81E1A  48 83 EC 30                     sub rsp, 0x30
00A81E1E  8B 82 D8 07 00 00               mov eax, dword ptr [rdx + 0x7d8]
00A81E24  48 8B DA                        mov rbx, rdx
00A81E27  A8 04                           test al, 4
00A81E29  75 07                           jne 0x140a81e32
00A81E2B  48 83 C4 30                     add rsp, 0x30
00A81E2F  5B                              pop rbx
00A81E30  C3                              ret
00A81E31  CC                              int3
00A81E32  83 F9 01                        cmp ecx, 1
00A81E35  C6 44 24 20 00                  mov byte ptr [rsp + 0x20], 0
00A81E3A  48 8D 05 57 9E 59 FF            lea rax, [rip - 0xa661a9]
00A81E41  8B D1                           mov edx, ecx
00A81E43  4C 8D 05 3E 9E 59 FF            lea r8, [rip - 0xa661c2]
00A81E4A  4C 8B CB                        mov r9, rbx
00A81E4D  4C 0F 45 C0                     cmovne r8, rax
00A81E51  B9 03 00 00 00                  mov ecx, 3
00A81E56  E8 11 00 00 00                  call 0x140a81e6c
00A81E5B  F0 83 A3 D8 07 00 00 FB         lock and dword ptr [rbx + 0x7d8], 0xfffffffb
00A81E63  EB C6                           jmp 0x140a81e2b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwTimLogProhibitFsctlSystemCalls(int a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int8 v_stack_p20;

    v_rsp = (v_rsp) - (48);
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(a2 + 2008)))) & (4)) != 0) goto loc_00A81E32;
loc_00A81E2B:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)(*(unsigned int *)(a2 + 2008));
loc_00A81E32:
    v_stack_p20 = 0;
    a3 = v_rip - 10904002;
    if (a1 != 1) { a3 = v_rip - 10903977; }
    result = EtwpTimLogMitigationForProcess(3, (unsigned int)(a1), a3, a2);
    goto loc_00A81E2B;
}
```

## 5. (Beta) C Style

```c
int64_t EtwTimLogProhibitFsctlSystemCalls(int32_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint8_t v_stack_p20;

    local_rsp = (local_rsp) - (48);
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(arg2 + 0x7D8)))) & (4)) != 0) goto loc_00A81E32;
loc_00A81E2B:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)(*(uint32_t *)(arg2 + 0x7D8));
loc_00A81E32:
    v_stack_p20 = 0;
    a3 = v_rip - 10904002;
    if (Arg1 != 1) { a3 = v_rip - 10903977; }
    result = EtwpTimLogMitigationForProcess(3, (uint32_t)(Arg1), a3, Arg2);
    goto loc_00A81E2B;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x7D8` | `32` | `R` |
| `Arg2` | `+ 0x7D8` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A81E18&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A81E18[BB_00A81E18]
  bb_00A81E2B[BB_00A81E2B]
  bb_00A81E31[BB_00A81E31]
  bb_00A81E32[BB_00A81E32]
  bb_00A81E18 -->|branch| bb_00A81E32
  bb_00A81E18 -->|fallthrough| bb_00A81E2B
  bb_00A81E31 -->|flow| bb_00A81E32
  bb_00A81E32 -->|branch| bb_00A81E2B
```
