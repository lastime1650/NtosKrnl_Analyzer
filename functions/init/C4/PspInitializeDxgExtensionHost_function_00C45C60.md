# PspInitializeDxgExtensionHost

- RVA: `0x00C45C60`–`0x00C45CDC` (길이 `124` bytes)
- VA: `0x0000000140C45C60`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009EAB4`
- 디코드: `31`개 명령, `124/124` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x00C45C75` → [Feature_ProcessDefaultQosNotifications__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_ProcessDefaultQosNotifications__private_IsEnabledDeviceUsageNoInline_function_005E24B4.md) (function, `0x005E24B4`)
- `0x00C45CC0` → [ExRegisterHost](../../page/7D/ExRegisterHost_function_007D06CC.md) (function, `0x007D06CC`)

### Direct callers
- [PspInitPhase1](PspInitPhase1_function_00C453B8.md) at `0x00C45431`

### Static image references
- `0x00C45C7E` → RVA `0x00008798` (`.rdata`; read)
- `0x00C45CA3` → RVA `0x00FC7038` (`ALMOSTRO`; read)
- `0x00C45CAA` → RVA `0x00781670` (`PspDxgExtensionHostCallback`; read)
- `0x00C45CC9` → RVA `0x00FC7038` (`ALMOSTRO`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00C45C75` → [Feature_ProcessDefaultQosNotifications__private_IsEnabledDeviceUsageNoInline](../../text/5E/Feature_ProcessDefaultQosNotifications__private_IsEnabledDeviceUsageNoInline_function_005E24B4.md) (`INIT` → `.text`)
  - `0x00C45CC0` → [ExRegisterHost](../../page/7D/ExRegisterHost_function_007D06CC.md) (`INIT` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C45C60  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00C45C65  55                              push rbp
00C45C66  48 8B EC                        mov rbp, rsp
00C45C69  48 83 EC 60                     sub rsp, 0x60
00C45C6D  33 DB                           xor ebx, ebx
00C45C6F  89 5D D4                        mov dword ptr [rbp - 0x2c], ebx
00C45C72  89 5D E4                        mov dword ptr [rbp - 0x1c], ebx
00C45C75  E8 3A C8 99 FF                  call 0x1405e24b4
00C45C7A  85 C0                           test eax, eax
00C45C7C  74 52                           je 0x140c45cd0
00C45C7E  48 8D 05 13 2B 3C FF            lea rax, [rip - 0xc3d4ed]
00C45C85  C7 45 C0 01 00 00 00            mov dword ptr [rbp - 0x40], 1
00C45C8C  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00C45C90  4C 8D 45 D0                     lea r8, [rbp - 0x30]
00C45C94  48 8D 45 C0                     lea rax, [rbp - 0x40]
00C45C98  C7 45 D0 13 00 01 00            mov dword ptr [rbp - 0x30], 0x10013
00C45C9F  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
00C45CA3  48 8D 0D 8E 13 38 00            lea rcx, [rip + 0x38138e]
00C45CAA  48 8D 05 BF B9 B3 FF            lea rax, [rip - 0x4c4641]
00C45CB1  C7 45 E0 00 02 00 00            mov dword ptr [rbp - 0x20], 0x200
00C45CB8  48 89 45 E8                     mov qword ptr [rbp - 0x18], rax
00C45CBC  48 89 5D F0                     mov qword ptr [rbp - 0x10], rbx
00C45CC0  E8 07 AA B8 FF                  call 0x1407d06cc
00C45CC5  85 C0                           test eax, eax
00C45CC7  79 07                           jns 0x140c45cd0
00C45CC9  48 89 1D 68 13 38 00            mov qword ptr [rip + 0x381368], rbx
00C45CD0  48 8B 5C 24 70                  mov rbx, qword ptr [rsp + 0x70]
00C45CD5  48 83 C4 60                     add rsp, 0x60
00C45CD9  5D                              pop rbp
00C45CDA  C3                              ret
00C45CDB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PspInitializeDxgExtensionHost(void)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned int v_stack_m24;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_m30;
    unsigned int v_stack_m34;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (96);
    v_rbx = 0;
    v_stack_m34 = 0;
    v_stack_m24 = 0;
    result = Feature_ProcessDefaultQosNotifications__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((unsigned int)(result) == 0) goto loc_00C45CD0;
    v_stack_m48 = 1;
    v_stack_m40 = v_rip - 12834029;
    v_stack_m38 = 0x10013ULL;
    v_stack_m30 = v_stack_m48;
    v_stack_m28 = 512;
    v_stack_m20 = v_rip - 4998721;
    v_stack_m18 = 0;
    result = ExRegisterHost(v_rip + 3675022, a2, v_stack_m38, a4);
    if (sign_flag) {
        *(unsigned __int64 *)(v_rip + 3674984) = 0;
    }
    v_rsp = (v_rsp) + (96);
    return result;
}
```

## 5. (Beta) C Style

```c
void PspInitializeDxgExtensionHost(void)
{
    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint32_t v_stack_m24;
    uint32_t v_stack_m28;
    uint64_t v_stack_m30;
    uint32_t v_stack_m34;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (96);
    local_rbx = 0;
    v_stack_m34 = 0;
    v_stack_m24 = 0;
    result = Feature_ProcessDefaultQosNotifications__private_IsEnabledDeviceUsageNoInline(a1, a2, a3, a4);
    if ((uint32_t)(result) == 0) goto loc_00C45CD0;
    v_stack_m48 = 1;
    v_stack_m40 = v_rip - 12834029;
    v_stack_m38 = 0x10013ULL;
    v_stack_m30 = v_stack_m48;
    v_stack_m28 = 512;
    v_stack_m20 = v_rip - 4998721;
    v_stack_m18 = 0;
    result = ExRegisterHost(v_rip + 3675022, a2, v_stack_m38, a4);
    if (sign_flag) {
        *(uint64_t *)(v_rip + 0x381368) = 0;
    }
    local_rsp = (local_rsp) + (96);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C45C60&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C45C60[BB_00C45C60]
  bb_00C45C7E[BB_00C45C7E]
  bb_00C45CC9[BB_00C45CC9]
  bb_00C45CD0[BB_00C45CD0]
  bb_00C45CDB[BB_00C45CDB]
  bb_00C45C60 -->|branch| bb_00C45CD0
  bb_00C45C60 -->|fallthrough| bb_00C45C7E
  bb_00C45C7E -->|branch| bb_00C45CD0
  bb_00C45C7E -->|fallthrough| bb_00C45CC9
  bb_00C45CC9 -->|flow| bb_00C45CD0
```
