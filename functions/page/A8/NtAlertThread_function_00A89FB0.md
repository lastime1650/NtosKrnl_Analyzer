# NtAlertThread

- RVA: `0x00A89FB0`–`0x00A8A024` (길이 `116` bytes)
- VA: `0x0000000140A89FB0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000B8510`
- 디코드: `29`개 명령, `116/116` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A89FF5` → [ObpReferenceObjectByHandleWithTag](../86/ObpReferenceObjectByHandleWithTag_function_00869650.md) (function, `0x00869650`)
- `0x00A8A00C` → [KeAlertThread](../../text/48/KeAlertThread_function_00489B40.md) (function, `0x00489B40`)
- `0x00A8A01B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (function, `0x002F78E0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00A89FD0` → RVA `0x00FC6AC8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A8A00C` → [KeAlertThread](../../text/48/KeAlertThread_function_00489B40.md) (`PAGE` → `.text`)
  - `0x00A8A01B` → [ObfDereferenceObjectWithTag](../../text/2F/ObfDereferenceObjectWithTag_function_002F78E0.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A89FB0  4C 8B DC                        mov r11, rsp
00A89FB3  53                              push rbx
00A89FB4  48 83 EC 40                     sub rsp, 0x40
00A89FB8  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
00A89FC1  BA 04 00 00 00                  mov edx, 4
00A89FC6  49 83 63 F0 00                  and qword ptr [r11 - 0x10], 0
00A89FCB  49 83 63 E8 00                  and qword ptr [r11 - 0x18], 0
00A89FD0  4C 8B 05 F1 CA 53 00            mov r8, qword ptr [rip + 0x53caf1]
00A89FD7  8A 98 32 02 00 00               mov bl, byte ptr [rax + 0x232]
00A89FDD  49 8D 43 10                     lea rax, [r11 + 0x10]
00A89FE1  49 83 63 10 00                  and qword ptr [r11 + 0x10], 0
00A89FE6  44 8A CB                        mov r9b, bl
00A89FE9  49 89 43 E0                     mov qword ptr [r11 - 0x20], rax
00A89FED  C7 44 24 20 50 73 53 75         mov dword ptr [rsp + 0x20], 0x75537350
00A89FF5  E8 56 F6 DD FF                  call 0x140869650
00A89FFA  85 C0                           test eax, eax
00A89FFC  79 07                           jns 0x140a8a005
00A89FFE  48 83 C4 40                     add rsp, 0x40
00A8A002  5B                              pop rbx
00A8A003  C3                              ret
00A8A004  CC                              int3
00A8A005  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A8A00A  8A D3                           mov dl, bl
00A8A00C  E8 2F FB 9F FF                  call 0x140489b40
00A8A011  48 8B 4C 24 58                  mov rcx, qword ptr [rsp + 0x58]
00A8A016  BA 50 73 53 75                  mov edx, 0x75537350
00A8A01B  E8 C0 D8 86 FF                  call 0x1402f78e0
00A8A020  33 C0                           xor eax, eax
00A8A022  EB DA                           jmp 0x140a89ffe
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall NtAlertThread(void)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m28;
    unsigned __int64 v_stack_p58;

    v_rsp = (v_rsp) - (64);
    *(unsigned __int64 *)(v_rsp - 32) = v_rsp + 16;
    v_stack_m28 = 0x75537350ULL;
    result = ObpReferenceObjectByHandleWithTag(a1, 4, *(unsigned __int64 *)(v_rip + 5491441), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    if (!sign_flag) goto loc_00A8A005;
loc_00A89FFE:
    v_rsp = (v_rsp) + (64);
    return result;
loc_00A8A005:
    result = KeAlertThread(v_stack_p58, (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)), *(unsigned __int64 *)(v_rip + 5491441), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    result = ObfDereferenceObjectWithTag(v_stack_p58, (unsigned int)(0x75537350ULL), *(unsigned __int64 *)(v_rip + 5491441), (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(gs_base + (0 + 392)) + 562)));
    result = 0;
    goto loc_00A89FFE;
}
```

## 5. (Beta) C Style

```c
void NtAlertThread(void)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m28;
    uint64_t v_stack_p58;

    local_rsp = (local_rsp) - (64);
    *(uint64_t *)(local_rsp - 0x20) = local_rsp + 16;
    v_stack_m28 = 0x75537350ULL;
    result = ObpReferenceObjectByHandleWithTag(a1, 4, *(uint64_t *)(v_rip + 0x53CAF1), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    if (!sign_flag) goto loc_00A8A005;
loc_00A89FFE:
    local_rsp = (local_rsp) + (64);
    return result;
loc_00A8A005:
    result = KeAlertThread(v_stack_p58, (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)), *(uint64_t *)(v_rip + 0x53CAF1), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    result = ObfDereferenceObjectWithTag(v_stack_p58, (uint32_t)(0x75537350ULL), *(uint64_t *)(v_rip + 0x53CAF1), (uint8_t)(*(uint8_t *)(*(uint64_t *)(gs_base + (0 + 0x188)) + 0x232)));
    result = 0;
    goto loc_00A89FFE;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A89FB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A89FB0[BB_00A89FB0]
  bb_00A89FFE[BB_00A89FFE]
  bb_00A8A004[BB_00A8A004]
  bb_00A8A005[BB_00A8A005]
  bb_00A89FB0 -->|branch| bb_00A8A005
  bb_00A89FB0 -->|fallthrough| bb_00A89FFE
  bb_00A8A004 -->|flow| bb_00A8A005
  bb_00A8A005 -->|branch| bb_00A89FFE
```
