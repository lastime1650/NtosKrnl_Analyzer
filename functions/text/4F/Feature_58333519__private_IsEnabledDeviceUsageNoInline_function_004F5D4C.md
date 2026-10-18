# Feature_58333519__private_IsEnabledDeviceUsageNoInline

- RVA: `0x004F5D4C`–`0x004F5D7E` (길이 `50` bytes)
- VA: `0x00000001404F5D4C`
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
- `0x004F5D73` → [Feature_58333519__private_IsEnabledFallback](Feature_58333519__private_IsEnabledFallback_function_004F5D84.md) (function, `0x004F5D84`)

### Direct callers
- [sub_00702150](../../page/70/Unknown_function_00702150.md) at `0x00702216`
- [sub_008D22F4](../../page/8D/Unknown_function_008D22F4.md) at `0x008D236A`
- [sub_00907768](../../page/90/Unknown_function_00907768.md) at `0x009078B9`
- [sub_00A67F9C](../../page/A6/Unknown_function_00A67F9C.md) at `0x00A68007`

### Static image references
- `0x004F5D56` → RVA `0x00FC4D40` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F5D4C  48 83 EC 28                     sub rsp, 0x28
004F5D50  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
004F5D56  8B 05 E4 EF AC 00               mov eax, dword ptr [rip + 0xacefe4]
004F5D5C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F5D60  A8 10                           test al, 0x10
004F5D62  74 05                           je 0x1404f5d69
004F5D64  83 E0 01                        and eax, 1
004F5D67  EB 0F                           jmp 0x1404f5d78
004F5D69  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
004F5D6E  BA 03 00 00 00                  mov edx, 3
004F5D73  E8 0C 00 00 00                  call 0x1404f5d84
004F5D78  48 83 C4 28                     add rsp, 0x28
004F5D7C  C3                              ret
004F5D7D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_58333519__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 11333604)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 11333604)))) & (16)) == 0) goto loc_004F5D69;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 11333604))) & (1));
    goto loc_004F5D78;
loc_004F5D69:
    result = Feature_58333519__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F5D78:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_58333519__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACEFE4)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xACEFE4)))) & (16)) == 0) goto loc_004F5D69;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xACEFE4))) & (1));
    goto loc_004F5D78;
loc_004F5D69:
    result = Feature_58333519__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_004F5D78:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F5D4C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F5D4C[BB_004F5D4C]
  bb_004F5D64[BB_004F5D64]
  bb_004F5D69[BB_004F5D69]
  bb_004F5D78[BB_004F5D78]
  bb_004F5D7D[BB_004F5D7D]
  bb_004F5D4C -->|branch| bb_004F5D69
  bb_004F5D4C -->|fallthrough| bb_004F5D64
  bb_004F5D64 -->|branch| bb_004F5D78
  bb_004F5D69 -->|flow| bb_004F5D78
```
