# McTemplateK0d_EtwWriteTransfer

- RVA: `0x00423380`–`0x004233DF` (길이 `95` bytes)
- VA: `0x0000000140423380`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0008E000`
- 디코드: `22`개 명령, `95/95` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **2**

### Outgoing calls
- `0x004233C7` → [McGenEventWrite_EtwWriteTransfer](McGenEventWrite_EtwWriteTransfer_function_00424FC8.md) (function, `0x00424FC8`)
- `0x004233D4` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [PiSwIrpStartCreate](../../page/8D/PiSwIrpStartCreate_function_008DA834.md) at `0x008DA986`
- [PiCMGetDeviceInterfaceList](../../page/A1/PiCMGetDeviceInterfaceList_function_00A163D0.md) at `0x00A16515`
- [PiCMGetDeviceIdList](../../page/A2/PiCMGetDeviceIdList_function_00A2BAAC.md) at `0x00A2BD5F`
- [PipInitComputerIds](../../init/C7/PipInitComputerIds_function_00C74734.md) at `0x00C75BD6`

### Static image references
- `0x0042338B` → RVA `0x00E0A740` (`.data`; read)
- `0x004233A8` → RVA `0x00E06DA0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00423380  4C 8B DC                        mov r11, rsp
00423383  45 89 4B 20                     mov dword ptr [r11 + 0x20], r9d
00423387  48 83 EC 68                     sub rsp, 0x68
0042338B  48 8B 05 AE 73 9E 00            mov rax, qword ptr [rip + 0x9e73ae]
00423392  48 33 C4                        xor rax, rsp
00423395  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
0042339A  49 8D 43 20                     lea rax, [r11 + 0x20]
0042339E  41 B9 02 00 00 00               mov r9d, 2
004233A4  49 89 43 D8                     mov qword ptr [r11 - 0x28], rax
004233A8  48 8D 0D F1 39 9E 00            lea rcx, [rip + 0x9e39f1]
004233AF  83 64 24 4C 00                  and dword ptr [rsp + 0x4c], 0
004233B4  49 8D 43 C8                     lea rax, [r11 - 0x38]
004233B8  45 33 C0                        xor r8d, r8d
004233BB  49 89 43 B8                     mov qword ptr [r11 - 0x48], rax
004233BF  C7 44 24 48 04 00 00 00         mov dword ptr [rsp + 0x48], 4
004233C7  E8 FC 1B 00 00                  call 0x140424fc8
004233CC  48 8B 4C 24 50                  mov rcx, qword ptr [rsp + 0x50]
004233D1  48 33 CC                        xor rcx, rsp
004233D4  E8 67 92 28 00                  call 0x1406ac640
004233D9  48 83 C4 68                     add rsp, 0x68
004233DD  C3                              ret
004233DE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall McTemplateK0d_EtwWriteTransfer(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m1C;
    unsigned int v_stack_m20;

    *(unsigned int *)(v_rsp + 32) = a4;
    v_rsp = (v_rsp) - (104);
    result = (*(unsigned __int64 *)(v_rip + 10384302)) ^ (v_rsp);
    v_stack_m18 = result;
    *(unsigned __int64 *)(v_rsp - 40) = v_rsp + 32;
    a3 = 0;
    *(unsigned __int64 *)(v_rsp - 72) = v_rsp - 56;
    v_stack_m20 = 4;
    result = McGenEventWrite_EtwWriteTransfer(v_rip + 10369521, a2, a3, 2);
    a1 = (v_stack_m18) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, 2);
    v_rsp = (v_rsp) + (104);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t McTemplateK0d_EtwWriteTransfer(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint32_t v_stack_m1C;
    uint32_t v_stack_m20;

    *(uint32_t *)(local_rsp + 0x20) = Arg4;
    local_rsp = (local_rsp) - (104);
    result = (*(uint64_t *)(v_rip + 0x9E73AE)) ^ (local_rsp);
    v_stack_m18 = result;
    *(uint64_t *)(local_rsp - 0x28) = local_rsp + 32;
    Arg3 = 0;
    *(uint64_t *)(local_rsp - 0x48) = local_rsp - 56;
    v_stack_m20 = 4;
    result = McGenEventWrite_EtwWriteTransfer(v_rip + 10369521, Arg2, Arg3, 2);
    Arg1 = (v_stack_m18) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, 2);
    local_rsp = (local_rsp) + (104);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00423380&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00423380[BB_00423380]
  bb_004233DE[BB_004233DE]
```
