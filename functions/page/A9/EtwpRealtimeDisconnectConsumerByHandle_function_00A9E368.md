# EtwpRealtimeDisconnectConsumerByHandle

- RVA: `0x00A9E368`–`0x00A9E3C8` (길이 `96` bytes)
- VA: `0x0000000140A9E368`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BA86C`
- 디코드: `25`개 명령, `96/96` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A9E39E` → [ObReferenceObjectByHandle](../86/ObReferenceObjectByHandle_function_00868DB0.md) (function, `0x00868DB0`)
- `0x00A9E3B7` → [EtwpRealtimeDisconnectConsumer](EtwpRealtimeDisconnectConsumer_function_00A9E3D0.md) (function, `0x00A9E3D0`)
- `0x00A9E3C1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (function, `0x002F9350`)

### Direct callers
- [NtTraceControl](NtTraceControl_function_00A9ED40.md) at `0x00A9F107`

### Static image references
- `0x00A9E383` → RVA `0x00FC53B0` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A9E3C1` → [ObfDereferenceObject](../../text/2F/ObfDereferenceObject_function_002F9350.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A9E368  4C 8B DC                        mov r11, rsp
00A9E36B  53                              push rbx
00A9E36C  48 83 EC 30                     sub rsp, 0x30
00A9E370  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A9E379  BA 00 04 00 00                  mov edx, 0x400
00A9E37E  49 83 63 F0 00                  and qword ptr [r11 - 0x10], 0
00A9E383  4C 8B 05 26 70 52 00            mov r8, qword ptr [rip + 0x527026]
00A9E38A  49 83 63 10 00                  and qword ptr [r11 + 0x10], 0
00A9E38F  44 8A 88 32 02 00 00            mov r9b, byte ptr [rax + 0x232]
00A9E396  49 8D 43 10                     lea rax, [r11 + 0x10]
00A9E39A  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00A9E39E  E8 0D AA DC FF                  call 0x140868db0
00A9E3A3  8B D8                           mov ebx, eax
00A9E3A5  85 C0                           test eax, eax
00A9E3A7  79 09                           jns 0x140a9e3b2
00A9E3A9  8B C3                           mov eax, ebx
00A9E3AB  48 83 C4 30                     add rsp, 0x30
00A9E3AF  5B                              pop rbx
00A9E3B0  C3                              ret
00A9E3B1  CC                              int3
00A9E3B2  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A9E3B7  E8 14 00 00 00                  call 0x140a9e3d0
00A9E3BC  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00A9E3C1  E8 8A AF 85 FF                  call 0x1402f9350
00A9E3C6  EB E1                           jmp 0x140a9e3a9
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwpRealtimeDisconnectConsumerByHandle(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p48;

    v_rsp = (v_rsp) - (48);
    *(unsigned __int64 *)(v_rsp - 24) = v_rsp + 16;
    result = ObReferenceObjectByHandle(a1, (unsigned int)(0x400ULL), *(unsigned __int64 *)(v_rip + 5402662), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (!sign_flag) goto loc_00A9E3B2;
loc_00A9E3A9:
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00A9E3B2:
    result = EtwpRealtimeDisconnectConsumer(v_stack_p48, (unsigned int)(0x400ULL), *(unsigned __int64 *)(v_rip + 5402662), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = ObfDereferenceObject(v_stack_p48, (unsigned int)(0x400ULL), *(unsigned __int64 *)(v_rip + 5402662), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    goto loc_00A9E3A9;
}
```

## 5. (Beta) C Style

```c
void EtwpRealtimeDisconnectConsumerByHandle(void)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p48;

    local_rsp = (local_rsp) - (48);
    *(uint64_t *)(local_rsp - 0x18) = local_rsp + 16;
    result = ObReferenceObjectByHandle(a1, (uint32_t)(0x400ULL), *(uint64_t *)(v_rip + 0x527026), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (!sign_flag) goto loc_00A9E3B2;
loc_00A9E3A9:
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00A9E3B2:
    result = EtwpRealtimeDisconnectConsumer(v_stack_p48, (uint32_t)(0x400ULL), *(uint64_t *)(v_rip + 0x527026), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = ObfDereferenceObject(v_stack_p48, (uint32_t)(0x400ULL), *(uint64_t *)(v_rip + 0x527026), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    goto loc_00A9E3A9;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A9E368&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A9E368[BB_00A9E368]
  bb_00A9E3A9[BB_00A9E3A9]
  bb_00A9E3B1[BB_00A9E3B1]
  bb_00A9E3B2[BB_00A9E3B2]
  bb_00A9E368 -->|branch| bb_00A9E3B2
  bb_00A9E368 -->|fallthrough| bb_00A9E3A9
  bb_00A9E3B1 -->|flow| bb_00A9E3B2
  bb_00A9E3B2 -->|branch| bb_00A9E3A9
```
