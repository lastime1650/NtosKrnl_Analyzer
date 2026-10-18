# EtwRegisterClassicProvider

- RVA: `0x00AA5B40`–`0x00AA5B87` (길이 `71` bytes)
- VA: `0x0000000140AA5B40`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BB7AC`
- 디코드: `18`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00AA5B80` → [EtwpRegisterKMProvider](../92/EtwpRegisterKMProvider_function_009209A4.md) (function, `0x009209A4`)

### Direct callers
- [WmipProcessLegacyEtwRegister](../7B/WmipProcessLegacyEtwRegister_function_007B3F64.md) at `0x007B3FED`

### Static image references
- `0x00AA5B6B` → RVA `0x00FC6AA8` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00AA5B40  48 83 EC 48                     sub rsp, 0x48
00AA5B44  48 8B D1                        mov rdx, rcx
00AA5B47  4D 85 C0                        test r8, r8
00AA5B4A  75 0B                           jne 0x140aa5b57
00AA5B4C  B8 0D 00 00 C0                  mov eax, 0xc000000d
00AA5B51  48 83 C4 48                     add rsp, 0x48
00AA5B55  C3                              ret
00AA5B56  CC                              int3
00AA5B57  48 8B 44 24 70                  mov rax, qword ptr [rsp + 0x70]
00AA5B5C  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00AA5B61  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00AA5B66  48 89 4C 24 28                  mov qword ptr [rsp + 0x28], rcx
00AA5B6B  48 8B 0D 36 0F 52 00            mov rcx, qword ptr [rip + 0x520f36]
00AA5B72  4C 89 4C 24 20                  mov qword ptr [rsp + 0x20], r9
00AA5B77  4D 8B C8                        mov r9, r8
00AA5B7A  41 B8 02 00 00 00               mov r8d, 2
00AA5B80  E8 1F AE E7 FF                  call 0x1409209a4
00AA5B85  EB CA                           jmp 0x140aa5b51
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall EtwRegisterClassicProvider(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p48;

    v_rsp = (v_rsp) - (72);
    if (a3 != 0) goto loc_00AA5B57;
loc_00AA5B51:
    v_rsp = (v_rsp) + (72);
    return (unsigned int)(0xC000000DULL);
loc_00AA5B57:
    v_stack_p30 = a5;
    v_stack_p28 = v_stack_p48;
    v_stack_p20 = a4;
    result = EtwpRegisterKMProvider(*(unsigned __int64 *)(v_rip + 5377846), a1, 2, a3);
    goto loc_00AA5B51;
}
```

## 5. (Beta) C Style

```c
int64_t EtwRegisterClassicProvider(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p48;

    local_rsp = (local_rsp) - (72);
    if (Arg3 != 0) goto loc_00AA5B57;
loc_00AA5B51:
    local_rsp = (local_rsp) + (72);
    return (uint32_t)(0xC000000DULL);
loc_00AA5B57:
    v_stack_p30 = Arg5;
    v_stack_p28 = v_stack_p48;
    v_stack_p20 = Arg4;
    result = EtwpRegisterKMProvider(*(uint64_t *)(v_rip + 0x520F36), Arg1, 2, Arg3);
    goto loc_00AA5B51;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00AA5B40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00AA5B40[BB_00AA5B40]
  bb_00AA5B4C[BB_00AA5B4C]
  bb_00AA5B51[BB_00AA5B51]
  bb_00AA5B56[BB_00AA5B56]
  bb_00AA5B57[BB_00AA5B57]
  bb_00AA5B40 -->|branch| bb_00AA5B57
  bb_00AA5B40 -->|fallthrough| bb_00AA5B4C
  bb_00AA5B4C -->|flow| bb_00AA5B51
  bb_00AA5B56 -->|flow| bb_00AA5B57
  bb_00AA5B57 -->|branch| bb_00AA5B51
```
