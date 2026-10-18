# CmpDiskFullWarningWorker

- RVA: `0x007E5A60`–`0x007E5A9A` (길이 `58` bytes)
- VA: `0x00000001407E5A60`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D2F4`
- 디코드: `15`개 명령, `58/58` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x007E5A6B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x007E5A8F` → [ExRaiseHardError](../A6/ExRaiseHardError_function_00A64520.md) (function, `0x00A64520`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x007E5A6B` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
007E5A60  48 83 EC 38                     sub rsp, 0x38
007E5A64  83 64 24 48 00                  and dword ptr [rsp + 0x48], 0
007E5A69  33 D2                           xor edx, edx
007E5A6B  E8 00 CE 39 00                  call 0x140b82870
007E5A70  48 8D 44 24 48                  lea rax, [rsp + 0x48]
007E5A75  45 33 C9                        xor r9d, r9d
007E5A78  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
007E5A7D  45 33 C0                        xor r8d, r8d
007E5A80  33 D2                           xor edx, edx
007E5A82  C7 44 24 20 01 00 00 00         mov dword ptr [rsp + 0x20], 1
007E5A8A  B9 7F 00 00 C0                  mov ecx, 0xc000007f
007E5A8F  E8 8C EA 27 00                  call 0x140a64520
007E5A94  48 83 C4 38                     add rsp, 0x38
007E5A98  C3                              ret
007E5A99  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmpDiskFullWarningWorker(__int64 a1, int a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned int v_stack_m18;
    unsigned int v_stack_p10;

    v_rsp = (v_rsp) - (56);
    a2 = 0;
    result = ExFreePoolWithTag(a1, a2, a3, a4);
    a4 = 0;
    v_stack_m10 = v_stack_p10;
    a3 = 0;
    a2 = 0;
    v_stack_m18 = 1;
    result = ExRaiseHardError((unsigned int)(0xC000007FULL), a2, a3, a4);
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmpDiskFullWarningWorker(int64_t Arg1, int32_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint32_t v_stack_m18;
    uint32_t v_stack_p10;

    local_rsp = (local_rsp) - (56);
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg1, Arg2, Arg3, Arg4);
    Arg4 = 0;
    v_stack_m10 = v_stack_p10;
    Arg3 = 0;
    Arg2 = 0;
    v_stack_m18 = 1;
    result = ExRaiseHardError((uint32_t)(0xC000007FULL), Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x007E5A60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_007E5A60[BB_007E5A60]
  bb_007E5A99[BB_007E5A99]
```
