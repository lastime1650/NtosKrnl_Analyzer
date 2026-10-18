# Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F2D58`–`0x004F2D8A` (길이 `50` bytes)
- VA: `0x00000001404F2D58`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004F2D7F` → [Feature_ShadowAdminAppCompat__private_IsEnabledFallback](../60/Feature_ShadowAdminAppCompat__private_IsEnabledFallback_function_00606720.md) (function, `0x00606720`)

### Direct callers
- [SeQueryInformationToken](../../page/8B/SeQueryInformationToken_function_008B5090.md) at `0x008B6366`
- [SeQueryInformationToken](../../page/8B/SeQueryInformationToken_function_008B5090.md) at `0x008B6383`
- [SepDuplicateToken](../../page/8B/SepDuplicateToken_function_008B87EC.md) at `0x008B8B4D`
- [SepFilterToken](../../page/9C/SepFilterToken_function_009C6B80.md) at `0x009C6FCA`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF0625`
- [NtSetInformationToken](../../page/AF/NtSetInformationToken_function_00AF0530.md) at `0x00AF138C`

### Static image references
- `0x004F2D62` → RVA `0x00FC4B20` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F2D58  48 83 EC 28                     sub rsp, 0x28
004F2D5C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F2D62  8B 05 B8 1D AD 00               mov eax, dword ptr [rip + 0xad1db8]
004F2D68  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F2D6C  A8 10                           test al, 0x10
004F2D6E  74 05                           je 0x1404f2d75
004F2D70  83 E0 01                        and eax, 1
004F2D73  EB 0F                           jmp 0x1404f2d84
004F2D75  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F2D7A  BA 03 00 00 00                  mov edx, 3
004F2D7F  E8 9C 39 11 00                  call 0x140606720
004F2D84  48 83 C4 28                     add rsp, 0x28
004F2D88  C3                              ret
004F2D89  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11345336)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11345336)))) & (16)) == 0) goto loc_004F2D75;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11345336))) & (1));
    goto loc_004F2D84;
loc_004F2D75:
    result = Feature_ShadowAdminAppCompat__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F2D84:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_ShadowAdminAppCompat__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD1DB8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xAD1DB8)))) & (16)) == 0) goto loc_004F2D75;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xAD1DB8))) & (1));
    goto loc_004F2D84;
loc_004F2D75:
    result = Feature_ShadowAdminAppCompat__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F2D84:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F2D58&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F2D58[BB_004F2D58]
  bb_004F2D70[BB_004F2D70]
  bb_004F2D75[BB_004F2D75]
  bb_004F2D84[BB_004F2D84]
  bb_004F2D89[BB_004F2D89]
  bb_004F2D58 -->|branch| bb_004F2D75
  bb_004F2D58 -->|fallthrough| bb_004F2D70
  bb_004F2D70 -->|branch| bb_004F2D84
  bb_004F2D75 -->|flow| bb_004F2D84
```
