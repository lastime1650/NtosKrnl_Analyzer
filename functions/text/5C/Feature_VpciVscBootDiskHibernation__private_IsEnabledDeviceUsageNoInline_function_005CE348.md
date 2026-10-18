# Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline

- RVA: `0x005CE348`–`0x005CE37A` (길이 `50` bytes)
- VA: `0x00000001405CE348`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x005CE36F` → [Feature_VpciVscBootDiskHibernation__private_IsEnabledFallback](Feature_VpciVscBootDiskHibernation__private_IsEnabledFallback_function_005CE380.md) (function, `0x005CE380`)

### Direct callers
- [PopAllocateHiberContext](../../page/AD/PopAllocateHiberContext_function_00ADC05C.md) at `0x00ADC0B5`
- [PoInitSystem](../../init/C7/PoInitSystem_function_00C72358.md) at `0x00C72985`

### Static image references
- `0x005CE352` → RVA `0x00FC4750` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005CE348  48 83 EC 28                     sub rsp, 0x28
005CE34C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005CE352  8B 05 F8 63 9F 00               mov eax, dword ptr [rip + 0x9f63f8]
005CE358  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005CE35C  A8 10                           test al, 0x10
005CE35E  74 05                           je 0x1405ce365
005CE360  83 E0 01                        and eax, 1
005CE363  EB 0F                           jmp 0x1405ce374
005CE365  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
005CE36A  BA 03 00 00 00                  mov edx, 3
005CE36F  E8 0C 00 00 00                  call 0x1405ce380
005CE374  48 83 C4 28                     add rsp, 0x28
005CE378  C3                              ret
005CE379  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10445816)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10445816)))) & (16)) == 0) goto loc_005CE365;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10445816))) & (1));
    goto loc_005CE374;
loc_005CE365:
    result = Feature_VpciVscBootDiskHibernation__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005CE374:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_VpciVscBootDiskHibernation__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9F63F8)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9F63F8)))) & (16)) == 0) goto loc_005CE365;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9F63F8))) & (1));
    goto loc_005CE374;
loc_005CE365:
    result = Feature_VpciVscBootDiskHibernation__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_005CE374:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005CE348&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005CE348[BB_005CE348]
  bb_005CE360[BB_005CE360]
  bb_005CE365[BB_005CE365]
  bb_005CE374[BB_005CE374]
  bb_005CE379[BB_005CE379]
  bb_005CE348 -->|branch| bb_005CE365
  bb_005CE348 -->|fallthrough| bb_005CE360
  bb_005CE360 -->|branch| bb_005CE374
  bb_005CE365 -->|flow| bb_005CE374
```
