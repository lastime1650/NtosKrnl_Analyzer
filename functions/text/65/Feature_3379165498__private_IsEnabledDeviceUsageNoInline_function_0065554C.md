# Feature_3379165498__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0065554C`–`0x0065557E` (길이 `50` bytes)
- VA: `0x000000014065554C`
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
- `0x00655573` → [Feature_3379165498__private_IsEnabledFallback](Feature_3379165498__private_IsEnabledFallback_function_00655584.md) (function, `0x00655584`)

### Direct callers
- [BapdpProcessVsmKeyBlobs](../../init/C4/BapdpProcessVsmKeyBlobs_function_00C4FD60.md) at `0x00C4FDB1`
- [BapdpProcessVsmKeyBlobs](../../init/C4/BapdpProcessVsmKeyBlobs_function_00C4FD60.md) at `0x00C4FDD1`
- [BapdpProcessVsmKeyBlobs](../../init/C4/BapdpProcessVsmKeyBlobs_function_00C4FD60.md) at `0x00C4FF52`

### Static image references
- `0x00655556` → RVA `0x00FC4C18` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065554C  48 83 EC 28                     sub rsp, 0x28
00655550  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00655556  8B 05 BC F6 96 00               mov eax, dword ptr [rip + 0x96f6bc]
0065555C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00655560  A8 10                           test al, 0x10
00655562  74 05                           je 0x140655569
00655564  83 E0 01                        and eax, 1
00655567  EB 0F                           jmp 0x140655578
00655569  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0065556E  BA 03 00 00 00                  mov edx, 3
00655573  E8 0C 00 00 00                  call 0x140655584
00655578  48 83 C4 28                     add rsp, 0x28
0065557C  C3                              ret
0065557D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_3379165498__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9893564)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9893564)))) & (16)) == 0) goto loc_00655569;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9893564))) & (1));
    goto loc_00655578;
loc_00655569:
    result = Feature_3379165498__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00655578:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_3379165498__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x96F6BC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x96F6BC)))) & (16)) == 0) goto loc_00655569;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x96F6BC))) & (1));
    goto loc_00655578;
loc_00655569:
    result = Feature_3379165498__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00655578:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065554C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065554C[BB_0065554C]
  bb_00655564[BB_00655564]
  bb_00655569[BB_00655569]
  bb_00655578[BB_00655578]
  bb_0065557D[BB_0065557D]
  bb_0065554C -->|branch| bb_00655569
  bb_0065554C -->|fallthrough| bb_00655564
  bb_00655564 -->|branch| bb_00655578
  bb_00655569 -->|flow| bb_00655578
```
