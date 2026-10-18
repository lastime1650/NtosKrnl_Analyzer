# Feature_3244801339__private_IsEnabledDeviceUsageNoInline

- RVA: `0x00581C88`–`0x00581CBA` (길이 `50` bytes)
- VA: `0x0000000140581C88`
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
- `0x00581CAF` → [Feature_3244801339__private_IsEnabledFallback](Feature_3244801339__private_IsEnabledFallback_function_00581CC0.md) (function, `0x00581CC0`)

### Direct callers
- [FsRtlpRequestShareableOplock](../4E/FsRtlpRequestShareableOplock_function_004E6EC8.md) at `0x004E7678`
- [FsRtlpRequestShareableOplock](../4E/FsRtlpRequestShareableOplock_function_004E6EC8.md) at `0x004E76AA`
- [FsRtlpRequestShareableOplock](../4E/FsRtlpRequestShareableOplock_function_004E6EC8.md) at `0x004E76D4`

### Static image references
- `0x00581C92` → RVA `0x00FC4730` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00581C88  48 83 EC 28                     sub rsp, 0x28
00581C8C  48 83 64 24 30 00               and qword ptr [rsp + 0x30], 0
00581C92  8B 05 98 2A A4 00               mov eax, dword ptr [rip + 0xa42a98]
00581C98  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00581C9C  A8 10                           test al, 0x10
00581C9E  74 05                           je 0x140581ca5
00581CA0  83 E0 01                        and eax, 1
00581CA3  EB 0F                           jmp 0x140581cb4
00581CA5  48 8B 4C 24 30                  mov rcx, qword ptr [rsp + 0x30]
00581CAA  BA 03 00 00 00                  mov edx, 3
00581CAF  E8 0C 00 00 00                  call 0x140581cc0
00581CB4  48 83 C4 28                     add rsp, 0x28
00581CB8  C3                              ret
00581CB9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall Feature_3244801339__private_IsEnabledDeviceUsageNoInline(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_rsp = (v_rsp) - (40);
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 10758808)));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(v_rip + 10758808)))) & (16)) == 0) goto loc_00581CA5;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(v_rip + 10758808))) & (1));
    goto loc_00581CB4;
loc_00581CA5:
    result = Feature_3244801339__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00581CB4:
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
void Feature_3244801339__private_IsEnabledDeviceUsageNoInline(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    local_rsp = (local_rsp) - (40);
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA42A98)));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(v_rip + 0xA42A98)))) & (16)) == 0) goto loc_00581CA5;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(v_rip + 0xA42A98))) & (1));
    goto loc_00581CB4;
loc_00581CA5:
    result = Feature_3244801339__private_IsEnabledFallback(v_stack_p8, 3, a3, a4);
loc_00581CB4:
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00581C88&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00581C88[BB_00581C88]
  bb_00581CA0[BB_00581CA0]
  bb_00581CA5[BB_00581CA5]
  bb_00581CB4[BB_00581CB4]
  bb_00581CB9[BB_00581CB9]
  bb_00581C88 -->|branch| bb_00581CA5
  bb_00581C88 -->|fallthrough| bb_00581CA0
  bb_00581CA0 -->|branch| bb_00581CB4
  bb_00581CA5 -->|flow| bb_00581CB4
```
