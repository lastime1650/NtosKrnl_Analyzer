# Feature_261863737__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0069D46C`–`0x0069D49E` (길이 `50` bytes)
- VA: `0x000000014069D46C`
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
- `0x0069D493` → [Feature_261863737__private_IsEnabledFallback](Feature_261863737__private_IsEnabledFallback_function_0069D4A4.md) (function, `0x0069D4A4`)

### Direct callers
- [AslpFileGetVersionBlockFromResourceRoot](../../page/81/AslpFileGetVersionBlockFromResourceRoot_function_0081FF98.md) at `0x008201AB`
- [AslpFileVerStringBlockGetValue](../../page/82/AslpFileVerStringBlockGetValue_function_00821370.md) at `0x008213CD`
- [AslpFileVerStringBlockGetValue](../../page/82/AslpFileVerStringBlockGetValue_function_00821370.md) at `0x008213F8`
- [AslpFileVerQueryBlock](../../page/AF/AslpFileVerQueryBlock_function_00AF9694.md) at `0x00AF985A`

### Static image references
- `0x0069D476` → RVA `0x00FC4E50` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0069D46C  48 83 EC 28                     sub rsp, 0x28
0069D470  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0069D476  8B 05 D4 79 92 00               mov eax, dword ptr [rip + 0x9279d4]
0069D47C  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0069D480  A8 10                           test al, 0x10
0069D482  74 05                           je 0x14069d489
0069D484  83 E0 01                        and eax, 1
0069D487  EB 0F                           jmp 0x14069d498
0069D489  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0069D48E  BA 03 00 00 00                  mov edx, 3
0069D493  E8 0C 00 00 00                  call 0x14069d4a4
0069D498  48 83 C4 28                     add rsp, 0x28
0069D49C  C3                              ret
0069D49D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_261863737__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9599444)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9599444)))) & (16)) == 0) goto loc_0069D489;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9599444))) & (1));
    goto loc_0069D498;
loc_0069D489:
    result = Feature_261863737__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0069D498:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_261863737__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9279D4)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x9279D4)))) & (16)) == 0) goto loc_0069D489;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x9279D4))) & (1));
    goto loc_0069D498;
loc_0069D489:
    result = Feature_261863737__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0069D498:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0069D46C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0069D46C[BB_0069D46C]
  bb_0069D484[BB_0069D484]
  bb_0069D489[BB_0069D489]
  bb_0069D498[BB_0069D498]
  bb_0069D49D[BB_0069D49D]
  bb_0069D46C -->|branch| bb_0069D489
  bb_0069D46C -->|fallthrough| bb_0069D484
  bb_0069D484 -->|branch| bb_0069D498
  bb_0069D489 -->|flow| bb_0069D498
```
