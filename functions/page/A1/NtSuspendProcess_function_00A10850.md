# NtSuspendProcess

- RVA: `0x00A10850`–`0x00A108C4` (길이 `116` bytes)
- VA: `0x0000000140A10850`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A929C`
- 디코드: `29`개 명령, `116/116` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A10893` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00A108AC` → [PsSuspendProcess](PsSuspendProcess_function_00A10F30.md) (function, `0x00A10F30`)
- `0x00A108BD` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A10870` → RVA `0x00FC6A98` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00A108BD` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A10850  4C 8B DC                        mov r11, rsp
00A10853  53                              push rbx
00A10854  48 83 EC 40                     sub rsp, 0x40
00A10858  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A10861  BA 00 08 00 00                  mov edx, 0x800
00A10866  49 83 63 F0 00                  and qword ptr [r11 - 0x10], 0
00A1086B  49 83 63 E8 00                  and qword ptr [r11 - 0x18], 0
00A10870  4C 8B 05 21 62 5B 00            mov r8, qword ptr [rip + 0x5b6221]
00A10877  44 8A 88 32 02 00 00            mov r9b, byte ptr [rax + 0x232]
00A1087E  49 8D 43 10                     lea rax, [r11 + 0x10]
00A10882  49 83 63 10 00                  and qword ptr [r11 + 0x10], 0
00A10887  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00A1088B  C7 44 24 20 50 73 53 75         mov dword ptr [rsp + 0x20], 0x75537350
00A10893  E8 B8 8D E5 FF                  call 0x140869650
00A10898  8B D8                           mov ebx, eax
00A1089A  85 C0                           test eax, eax
00A1089C  79 09                           jns 0x140a108a7
00A1089E  8B C3                           mov eax, ebx
00A108A0  48 83 C4 40                     add rsp, 0x40
00A108A4  5B                              pop rbx
00A108A5  C3                              ret
00A108A6  CC                              int3
00A108A7  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A108AC  E8 7F 06 00 00                  call 0x140a10f30
00A108B1  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A108B6  BA 50 73 53 75                  mov edx, 0x75537350
00A108BB  8B D8                           mov ebx, eax
00A108BD  E8 1E 70 8E FF                  call 0x1402f78e0
00A108C2  EB DA                           jmp 0x140a1089e
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtSuspendProcess(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p58;

    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 32) = v_rsp + 16;
    v_stack_m28 = 0x75537350ULL;
    result = ObpReferenceObjectByHandleWithTag(a1, (unsigned int)(0x800ULL), *(unsigned __int64 *)(v_rip + 5988897), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    if (!sign_flag) goto loc_00A108A7;
loc_00A1089E:
    v_rsp = (v_rsp) + (64);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
loc_00A108A7:
    result = PsSuspendProcess(v_stack_p58, (unsigned int)(0x800ULL), *(unsigned __int64 *)(v_rip + 5988897), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    result = ObfDereferenceObjectWithTag(v_stack_p58, (unsigned int)(0x75537350ULL), *(unsigned __int64 *)(v_rip + 5988897), *(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562));
    goto loc_00A1089E;
}
```

## 5. (Beta) C Style

```c
void NtSuspendProcess(void)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m28;
    uint64_t v_stack_p58;

    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x20) = local_rsp + 16;
    v_stack_m28 = 0x75537350ULL;
    result = ObpReferenceObjectByHandleWithTag(a1, (uint32_t)(0x800ULL), *(uint64_t *)(v_rip + 0x5B6221), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    if (!sign_flag) goto loc_00A108A7;
loc_00A1089E:
    local_rsp = (local_rsp) + (64);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
loc_00A108A7:
    result = PsSuspendProcess(v_stack_p58, (uint32_t)(0x800ULL), *(uint64_t *)(v_rip + 0x5B6221), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    result = ObfDereferenceObjectWithTag(v_stack_p58, (uint32_t)(0x75537350ULL), *(uint64_t *)(v_rip + 0x5B6221), *(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232));
    goto loc_00A1089E;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A10850&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A10850[BB_00A10850]
  bb_00A1089E[BB_00A1089E]
  bb_00A108A6[BB_00A108A6]
  bb_00A108A7[BB_00A108A7]
  bb_00A10850 -->|branch| bb_00A108A7
  bb_00A10850 -->|fallthrough| bb_00A1089E
  bb_00A108A6 -->|flow| bb_00A108A7
  bb_00A108A7 -->|branch| bb_00A1089E
```
