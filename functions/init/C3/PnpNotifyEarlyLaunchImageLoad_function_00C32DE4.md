# PnpNotifyEarlyLaunchImageLoad

- RVA: `0x00C32DE4`–`0x00C32E5B` (길이 `119` bytes)
- VA: `0x0000000140C32DE4`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BCD70`
- 디코드: `27`개 명령, `119/119` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00C32E02` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x00C32E44` → [ExNotifyWithProcessing](../../text/45/ExNotifyWithProcessing_function_004523F4.md) (function, `0x004523F4`)

### Direct callers
- [PipInitializeDriverDependentDLLs](../C7/PipInitializeDriverDependentDLLs_function_00C74398.md) at `0x00C744D7`
- [PnpInitializeBootStartDriver](../C7/PnpInitializeBootStartDriver_function_00C760F0.md) at `0x00C761C1`

### Static image references
- `0x00C32E07` → RVA `0x010086C0` (`INITDATA`; read)
- `0x00C32E13` → RVA `0x00C32D10` (`PnpEarlyLaunchImageNotificationPreProcess`; read)
- `0x00C32E29` → RVA `0x00C32C40` (`PnpEarlyLaunchImageNotificationPostProcess`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00C32E02` → [memset](../../text/6C/memset_function_006C6C40.md) (`INIT` → `.text`)
  - `0x00C32E44` → [ExNotifyWithProcessing](../../text/45/ExNotifyWithProcessing_function_004523F4.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C32DE4  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C32DE9  57                              push rdi
00C32DEA  48 81 EC B0 00 00 00            sub rsp, 0xb0
00C32DF1  48 8B DA                        mov rbx, rdx
00C32DF4  48 8B F9                        mov rdi, rcx
00C32DF7  33 D2                           xor edx, edx
00C32DF9  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
00C32DFE  44 8D 42 68                     lea r8d, [rdx + 0x68]
00C32E02  E8 39 3E A9 FF                  call 0x1406c6c40
00C32E07  48 8B 0D B2 58 3D 00            mov rcx, qword ptr [rip + 0x3d58b2]
00C32E0E  48 85 C9                        test rcx, rcx
00C32E11  74 36                           je 0x140c32e49
00C32E13  48 8D 05 F6 FE FF FF            lea rax, [rip - 0x10a]
00C32E1A  48 89 5C 24 30                  mov qword ptr [rsp + 0x30], rbx
00C32E1F  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00C32E24  4C 8D 4C 24 20                  lea r9, [rsp + 0x20]
00C32E29  48 8D 05 10 FE FF FF            lea rax, [rip - 0x1f0]
00C32E30  48 89 7C 24 38                  mov qword ptr [rsp + 0x38], rdi
00C32E35  4C 8D 44 24 40                  lea r8, [rsp + 0x40]
00C32E3A  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00C32E3F  BA 01 00 00 00                  mov edx, 1
00C32E44  E8 AB F5 81 FF                  call 0x1404523f4
00C32E49  48 8B 9C 24 C0 00 00 00         mov rbx, qword ptr [rsp + 0xc0]
00C32E51  48 81 C4 B0 00 00 00            add rsp, 0xb0
00C32E58  5F                              pop rdi
00C32E59  C3                              ret
00C32E5A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PnpNotifyEarlyLaunchImageLoad(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (176);
    a2 = 0;
    result = memset(v_stack_m78, a2, a2 + 104, a4);
    if (*(unsigned __int64 *)(v_rip + 4020402) != 0) {
        result = v_rip - 266;
        v_stack_m88 = 0;
        v_stack_m98 = result;
        a4 = v_stack_m98;
        result = v_rip - 496;
        v_stack_m80 = a1;
        a3 = v_stack_m78;
        v_stack_m90 = result;
        a2 = 1;
        result = ExNotifyWithProcessing(*(unsigned __int64 *)(v_rip + 4020402), a2, a3, a4);
    }
    v_rsp = (v_rsp) + (176);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PnpNotifyEarlyLaunchImageLoad(int64_t Arg1, int64_t Arg2)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (176);
    Arg2 = 0;
    result = memset(v_stack_m78, Arg2, Arg2 + 104, a4);
    if (*(uint64_t *)(v_rip + 0x3D58B2) != 0) {
        result = v_rip - 266;
        v_stack_m88 = 0;
        v_stack_m98 = result;
        a4 = v_stack_m98;
        result = v_rip - 496;
        v_stack_m80 = Arg1;
        a3 = v_stack_m78;
        v_stack_m90 = result;
        Arg2 = 1;
        result = ExNotifyWithProcessing(*(uint64_t *)(v_rip + 0x3D58B2), Arg2, a3, a4);
    }
    local_rsp = (local_rsp) + (176);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C32DE4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C32DE4[BB_00C32DE4]
  bb_00C32E13[BB_00C32E13]
  bb_00C32E49[BB_00C32E49]
  bb_00C32E5A[BB_00C32E5A]
  bb_00C32DE4 -->|branch| bb_00C32E49
  bb_00C32DE4 -->|fallthrough| bb_00C32E13
  bb_00C32E13 -->|flow| bb_00C32E49
```
