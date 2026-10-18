# Feature_AppContainerVolumeDeviceAccess__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0059788C`–`0x005978BE` (길이 `50` bytes)
- VA: `0x000000014059788C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005978B3` → [Feature_AppContainerVolumeDeviceAccess__private_IsEnabledFallback](Feature_AppContainerVolumeDeviceAccess__private_IsEnabledFallback_function_005978C4.md) (function, `0x005978C4`)

### Direct callers
- [IopCreateDefaultDeviceSecurityDescriptor](../../page/9A/IopCreateDefaultDeviceSecurityDescriptor_function_009A5008.md) at `0x009A520A`
- [IopCreateSecurityDescriptorPerType](../../page/AD/IopCreateSecurityDescriptorPerType_function_00ADCC6C.md) at `0x00ADCCB3`
- [SepInitSystemDacls](../../init/C4/SepInitSystemDacls_function_00C478DC.md) at `0x00C4793C`
- [SepInitSystemDacls](../../init/C4/SepInitSystemDacls_function_00C478DC.md) at `0x00C47A47`
- [SepInitSystemDacls](../../init/C4/SepInitSystemDacls_function_00C478DC.md) at `0x00C47B3C`
- [SepInitSystemDacls](../../init/C4/SepInitSystemDacls_function_00C478DC.md) at `0x00C47B69`
- [SepInitSystemDacls](../../init/C4/SepInitSystemDacls_function_00C478DC.md) at `0x00C47C4C`
- [SepInitSystemDacls](../../init/C4/SepInitSystemDacls_function_00C478DC.md) at `0x00C47D0D`
- [SepInitSystemDacls](../../init/C4/SepInitSystemDacls_function_00C478DC.md) at `0x00C47DDB`
- [SepInitSystemDacls](../../init/C4/SepInitSystemDacls_function_00C478DC.md) at `0x00C47E8F`
- [SepInitSystemDacls](../../init/C4/SepInitSystemDacls_function_00C478DC.md) at `0x00C480BB`

### Static image references
- `0x00597896` → RVA `0x00FC47B8` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0059788C  48 83 EC 28                     sub rsp, 0x28
00597890  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00597896  8B 05 1C CF A2 00               mov eax, dword ptr [rip + 0xa2cf1c]
0059789C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005978A0  A8 10                           test al, 0x10
005978A2  74 05                           je 0x1405978a9
005978A4  83 E0 01                        and eax, 1
005978A7  EB 0F                           jmp 0x1405978b8
005978A9  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005978AE  BA 03 00 00 00                  mov edx, 3
005978B3  E8 0C 00 00 00                  call 0x1405978c4
005978B8  48 83 C4 28                     add rsp, 0x28
005978BC  C3                              ret
005978BD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_AppContainerVolumeDeviceAccess__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10669852)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10669852)))) & (16)) == 0) goto loc_005978A9;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10669852))) & (1));
    goto loc_005978B8;
loc_005978A9:
    result = Feature_AppContainerVolumeDeviceAccess__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005978B8:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_AppContainerVolumeDeviceAccess__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA2CF1C)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA2CF1C)))) & (16)) == 0) goto loc_005978A9;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA2CF1C))) & (1));
    goto loc_005978B8;
loc_005978A9:
    result = Feature_AppContainerVolumeDeviceAccess__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005978B8:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0059788C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0059788C[BB_0059788C]
  bb_005978A4[BB_005978A4]
  bb_005978A9[BB_005978A9]
  bb_005978B8[BB_005978B8]
  bb_005978BD[BB_005978BD]
  bb_0059788C -->|branch| bb_005978A9
  bb_0059788C -->|fallthrough| bb_005978A4
  bb_005978A4 -->|branch| bb_005978B8
  bb_005978A9 -->|flow| bb_005978B8
```
