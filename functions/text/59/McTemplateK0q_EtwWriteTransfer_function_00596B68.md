# McTemplateK0q_EtwWriteTransfer

- RVA: `0x00596B68`–`0x00596BC0` (길이 `88` bytes)
- VA: `0x0000000140596B68`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008E000`
- 디코드: `21`개 명령, `88/88` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00596BA8` → [McGenEventWrite_EtwWriteTransfer](../42/McGenEventWrite_EtwWriteTransfer_function_00424FC8.md) (function, `0x00424FC8`)
- `0x00596BB5` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [SecureDump_LogErrorEvent](../5A/SecureDump_LogErrorEvent_function_005A314C.md) at `0x005A316A`
- [PnpCallAddDevice](../../page/8F/PnpCallAddDevice_function_008FC164.md) at `0x008FC284`
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2B7B8`
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2BB6B`
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2BCE2`
- [IoInitSystemPreDrivers](../../init/C2/IoInitSystemPreDrivers_function_00C2AC3C.md) at `0x00C2BEA5`

### Static image references
- `0x00596B73` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00596B68  4C 8B DC                        mov r11, rsp
00596B6B  45 89 4B 20                     mov dword ptr [r11 + 0x20], r9d
00596B6F  48 83 EC 68                     sub rsp, 0x68
00596B73  48 8B 05 C6 3B 87 00            mov rax, qword ptr [rip + 0x873bc6]
00596B7A  48 33 C4                        xor rax, rsp
00596B7D  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00596B82  49 8D 43 20                     lea rax, [r11 + 0x20]
00596B86  41 B9 02 00 00 00               mov r9d, 2
00596B8C  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
00596B90  45 33 C0                        xor r8d, r8d
00596B93  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
00596B98  49 8D 43 C8                     lea rax, [r11 - 0x38]
00596B9C  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
00596BA0  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
00596BA8  E8 1B E4 E8 FF                  call 0x140424fc8
00596BAD  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
00596BB2  48 33 CC                        xor rcx, rsp
00596BB5  E8 86 5A 11 00                  call 0x1406ac640
00596BBA  48 83 C4 68                     add rsp, 0x68
00596BBE  C3                              ret
00596BBF  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall McTemplateK0q_EtwWriteTransfer(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;

    *(unsigned int *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 8862662)) ^ (v_rsp);
    v_stack_m18 = result;
    *(unsigned __int64 *)(v_rsp - 40) = v_rsp + 32;
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 72) = v_rsp - 56;
    v_stack_m20 = 4;
    result = McGenEventWrite_EtwWriteTransfer(a1, a2, a3, 2);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, 2);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t McTemplateK0q_EtwWriteTransfer(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x873BC6)) ^ (local_rsp);
    v_stack_m18 = result;
    *(uint64_t *)(local_rsp - 0x28) = local_rsp + 32;
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x48) = local_rsp - 56;
    v_stack_m20 = 4;
    result = McGenEventWrite_EtwWriteTransfer(Arg1, Arg2, Arg3, 2);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, 2);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00596B68&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00596B68[BB_00596B68]
  bb_00596BBF[BB_00596BBF]
```
