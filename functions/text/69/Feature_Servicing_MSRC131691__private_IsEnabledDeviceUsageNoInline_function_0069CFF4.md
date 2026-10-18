# Feature_Servicing_MSRC131691__private_IsEnabledDeviceUsageNoInline

- RVA: `0x0069CFF4`–`0x0069D026` (길이 `50` bytes)
- VA: `0x000000014069CFF4`
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
- `0x0069D01B` → [Feature_Servicing_MSRC131691__private_IsEnabledFallback](Feature_Servicing_MSRC131691__private_IsEnabledFallback_function_0069D02C.md) (function, `0x0069D02C`)

### Direct callers
- [AslpFileGetImageNtHeader](../../page/81/AslpFileGetImageNtHeader_function_0081F434.md) at `0x0081F484`
- [AslpFileQuery16BitDescription](../../page/82/AslpFileQuery16BitDescription_function_00820B70.md) at `0x00820BA7`
- [AslpFileQuery16BitDescription](../../page/82/AslpFileQuery16BitDescription_function_00820B70.md) at `0x00820BC8`
- [AslpFileQuery16BitDescription](../../page/82/AslpFileQuery16BitDescription_function_00820B70.md) at `0x00820C39`
- [AslpFileQuery16BitModuleName](../../page/82/AslpFileQuery16BitModuleName_function_00820D08.md) at `0x00820D43`
- [AslpFileQuery16BitModuleName](../../page/82/AslpFileQuery16BitModuleName_function_00820D08.md) at `0x00820D64`
- [AslpFileQuery16BitModuleName](../../page/82/AslpFileQuery16BitModuleName_function_00820D08.md) at `0x00820E1B`
- [AslpFileMappingGetFileKind](../../page/AF/AslpFileMappingGetFileKind_function_00AF950C.md) at `0x00AF9587`

### Static image references
- `0x0069CFFE` → RVA `0x00FC4E48` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0069CFF4  48 83 EC 28                     sub rsp, 0x28
0069CFF8  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
0069CFFE  8B 05 44 7E 92 00               mov eax, dword ptr [rip + 0x927e44]
0069D004  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0069D008  A8 10                           test al, 0x10
0069D00A  74 05                           je 0x14069d011
0069D00C  83 E0 01                        and eax, 1
0069D00F  EB 0F                           jmp 0x14069d020
0069D011  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
0069D016  BA 03 00 00 00                  mov edx, 3
0069D01B  E8 0C 00 00 00                  call 0x14069d02c
0069D020  48 83 C4 28                     add rsp, 0x28
0069D024  C3                              ret
0069D025  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_Servicing_MSRC131691__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 9600580)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 9600580)))) & (16)) == 0) goto loc_0069D011;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 9600580))) & (1));
    goto loc_0069D020;
loc_0069D011:
    result = Feature_Servicing_MSRC131691__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0069D020:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_Servicing_MSRC131691__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0x927E44)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0x927E44)))) & (16)) == 0) goto loc_0069D011;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0x927E44))) & (1));
    goto loc_0069D020;
loc_0069D011:
    result = Feature_Servicing_MSRC131691__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_0069D020:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0069CFF4&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0069CFF4[BB_0069CFF4]
  bb_0069D00C[BB_0069D00C]
  bb_0069D011[BB_0069D011]
  bb_0069D020[BB_0069D020]
  bb_0069D025[BB_0069D025]
  bb_0069CFF4 -->|branch| bb_0069D011
  bb_0069CFF4 -->|fallthrough| bb_0069D00C
  bb_0069D00C -->|branch| bb_0069D020
  bb_0069D011 -->|flow| bb_0069D020
```
