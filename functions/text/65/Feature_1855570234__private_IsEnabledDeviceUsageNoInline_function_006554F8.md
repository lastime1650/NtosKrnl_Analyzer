# Feature_1855570234__private_IsEnabledDeviceUsageNoInline

- RVA: `0x006554F8`–`0x0065552A` (길이 `50` bytes)
- VA: `0x00000001406554F8`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `14`개 명령, `50/50` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0065551F` → [Feature_1855570234__private_IsEnabledFallback](Feature_1855570234__private_IsEnabledFallback_function_00655530.md) (function, `0x00655530`)

### Direct callers
- [BapdpProcessVsmKeyBlobs](../../init/C4/BapdpProcessVsmKeyBlobs_function_00C4FD60.md) at `0x00C4FDBA`
- [BapdpProcessVsmKeyBlobs](../../init/C4/BapdpProcessVsmKeyBlobs_function_00C4FD60.md) at `0x00C4FDDA`

### Static image references
- `0x00655502` → RVA `0x00FC4C10` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006554F8  48 83 EC 28                     sub rsp, 0x28
006554FC  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00655502  8B 05 08 F7 96 00               mov eax, dword ptr [rip + 0x96f708]
00655508  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0065550C  A8 10                           test al, 0x10
0065550E  74 05                           je 0x140655515
00655510  83 E0 01                        and eax, 1
00655513  EB 0F                           jmp 0x140655524
00655515  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0065551A  BA 03 00 00 00                  mov edx, 3
0065551F  E8 0C 00 00 00                  call 0x140655530
00655524  48 83 C4 28                     add rsp, 0x28
00655528  C3                              ret
00655529  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_1855570234__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9893640)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9893640)))) & (16)) == 0) goto loc_00655515;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9893640))) & (1));
    goto loc_00655524;
loc_00655515:
    result = Feature_1855570234__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00655524:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_1855570234__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x96F708)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x96F708)))) & (16)) == 0) goto loc_00655515;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x96F708))) & (1));
    goto loc_00655524;
loc_00655515:
    result = Feature_1855570234__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00655524:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006554F8&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_006554F8[BB_006554F8]
  bb_00655510[BB_00655510]
  bb_00655515[BB_00655515]
  bb_00655524[BB_00655524]
  bb_00655529[BB_00655529]
  bb_006554F8 -->|branch| bb_00655515
  bb_006554F8 -->|fallthrough| bb_00655510
  bb_00655510 -->|branch| bb_00655524
  bb_00655515 -->|flow| bb_00655524
```
