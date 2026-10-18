# Feature_1565498680__private_IsEnabledDeviceUsageNoInline

- RVA: `0x005977E4`–`0x00597816` (길이 `50` bytes)
- VA: `0x00000001405977E4`
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
- `0x0059780B` → [Feature_1565498680__private_IsEnabledFallback](Feature_1565498680__private_IsEnabledFallback_function_0059781C.md) (function, `0x0059781C`)

### Direct callers
- [IopfCompleteRequest](../29/IopfCompleteRequest_function_0029B5F8.md) at `0x0029BAB3`

### Static image references
- `0x005977EE` → RVA `0x00FC47D0` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005977E4  48 83 EC 28                     sub rsp, 0x28
005977E8  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
005977EE  8B 05 DC CF A2 00               mov eax, dword ptr [rip + 0xa2cfdc]
005977F4  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
005977F8  A8 10                           test al, 0x10
005977FA  74 05                           je 0x140597801
005977FC  83 E0 01                        and eax, 1
005977FF  EB 0F                           jmp 0x140597810
00597801  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00597806  BA 03 00 00 00                  mov edx, 3
0059780B  E8 0C 00 00 00                  call 0x14059781c
00597810  48 83 C4 28                     add rsp, 0x28
00597814  C3                              ret
00597815  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_1565498680__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10670044)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10670044)))) & (16)) == 0) goto loc_00597801;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10670044))) & (1));
    goto loc_00597810;
loc_00597801:
    result = Feature_1565498680__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00597810:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_1565498680__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA2CFDC)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA2CFDC)))) & (16)) == 0) goto loc_00597801;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA2CFDC))) & (1));
    goto loc_00597810;
loc_00597801:
    result = Feature_1565498680__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00597810:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005977E4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005977E4[BB_005977E4]
  bb_005977FC[BB_005977FC]
  bb_00597801[BB_00597801]
  bb_00597810[BB_00597810]
  bb_00597815[BB_00597815]
  bb_005977E4 -->|branch| bb_00597801
  bb_005977E4 -->|fallthrough| bb_005977FC
  bb_005977FC -->|branch| bb_00597810
  bb_00597801 -->|flow| bb_00597810
```
