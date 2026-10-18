# PopErratumUpdateCallback

- RVA: `0x005D4760`–`0x005D47A2` (길이 `66` bytes)
- VA: `0x00000001405D4760`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00097934`
- 디코드: `18`개 명령, `66/66` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005D477A` → [ExQueryWnfStateData](../../page/A4/ExQueryWnfStateData_function_00A4A480.md) (function, `0x00A4A480`)
- `0x005D4795` → [PopSetPowerSettingValueAcDc](../../page/91/PopSetPowerSettingValueAcDc_function_00914D6C.md) (function, `0x00914D6C`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x005D477A` → [ExQueryWnfStateData](../../page/A4/ExQueryWnfStateData_function_00A4A480.md) (`.text` → `PAGE`)
  - `0x005D4795` → [PopSetPowerSettingValueAcDc](../../page/91/PopSetPowerSettingValueAcDc_function_00914D6C.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005D4760  48 8B C4                        mov rax, rsp
005D4763  48 83 EC 38                     sub rsp, 0x38
005D4767  4C 8D 48 E8                     lea r9, [rax - 0x18]
005D476B  C7 40 E8 04 00 00 00            mov dword ptr [rax - 0x18], 4
005D4772  4C 8D 40 EC                     lea r8, [rax - 0x14]
005D4776  48 8D 50 F0                     lea rdx, [rax - 0x10]
005D477A  E8 01 5D 47 00                  call 0x140a4a480
005D477F  85 C0                           test eax, eax
005D4781  78 17                           js 0x1405d479a
005D4783  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
005D4788  4C 8D 44 24 24                  lea r8, [rsp + 0x24]
005D478D  8B 54 24 20                     mov edx, dword ptr [rsp + 0x20]
005D4791  48 83 C1 10                     add rcx, 0x10
005D4795  E8 D2 05 34 00                  call 0x140914d6c
005D479A  33 C0                           xor eax, eax
005D479C  48 83 C4 38                     add rsp, 0x38
005D47A0  C3                              ret
005D47A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopErratumUpdateCallback(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m14;
    unsigned int v_stack_m18;

    v_rsp = (v_rsp) - (56);
    *(unsigned int *)(v_rsp - 24) = 4;
    result = ExQueryWnfStateData(a1, v_rsp - 16, v_rsp - 20, v_rsp - 24);
    if (!(sign_flag)) {
        a1 = a6;
        a3 = v_stack_m14;
        a2 = v_stack_m18;
        a1 = (a1) + (16);
        result = PopSetPowerSettingValueAcDc(a1, a2, a3, v_rsp - 24);
    }
    result = 0;
    v_rsp = (v_rsp) + (56);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopErratumUpdateCallback(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m14;
    uint32_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    *(uint32_t *)(local_rsp - 0x18) = 4;
    result = ExQueryWnfStateData(Arg1, local_rsp - 16, local_rsp - 20, local_rsp - 24);
    if (!(sign_flag)) {
        Arg1 = Arg6;
        Arg3 = v_stack_m14;
        Arg2 = v_stack_m18;
        Arg1 = (Arg1) + (16);
        result = PopSetPowerSettingValueAcDc(Arg1, Arg2, Arg3, local_rsp - 24);
    }
    result = 0;
    local_rsp = (local_rsp) + (56);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005D4760&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005D4760[BB_005D4760]
  bb_005D4783[BB_005D4783]
  bb_005D479A[BB_005D479A]
  bb_005D47A1[BB_005D47A1]
  bb_005D4760 -->|branch| bb_005D479A
  bb_005D4760 -->|fallthrough| bb_005D4783
  bb_005D4783 -->|flow| bb_005D479A
```
