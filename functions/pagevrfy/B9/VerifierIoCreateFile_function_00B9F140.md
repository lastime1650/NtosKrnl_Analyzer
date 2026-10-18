# VerifierIoCreateFile

- RVA: `0x00B9F140`–`0x00B9F1DF` (길이 `159` bytes)
- VA: `0x0000000140B9F140`
- 실행 섹션: `PAGEVRFY`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000BA960`
- 디코드: `32`개 명령, `159/159` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00B9F1D0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00B9F198` → RVA `0x00FFEAF8` (`PAGEVRFD`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B9F1D0` → [guard_dispatch_icall](../../text/6B/guard_dispatch_icall_function_006BAAD0.md) (`PAGEVRFY` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00B9F140  40 53                           push rbx
00B9F142  48 81 EC 80 00 00 00            sub rsp, 0x80
00B9F149  8B 84 24 F8 00 00 00            mov eax, dword ptr [rsp + 0xf8]
00B9F150  48 8B D9                        mov rbx, rcx
00B9F153  8B 8C 24 C8 00 00 00            mov ecx, dword ptr [rsp + 0xc8]
00B9F15A  44 8B DA                        mov r11d, edx
00B9F15D  8B 94 24 D0 00 00 00            mov edx, dword ptr [rsp + 0xd0]
00B9F164  89 44 24 68                     mov dword ptr [rsp + 0x68], eax
00B9F168  48 8B 84 24 F0 00 00 00         mov rax, qword ptr [rsp + 0xf0]
00B9F170  48 89 44 24 60                  mov qword ptr [rsp + 0x60], rax
00B9F175  8B 84 24 E8 00 00 00            mov eax, dword ptr [rsp + 0xe8]
00B9F17C  89 44 24 58                     mov dword ptr [rsp + 0x58], eax
00B9F180  8B 84 24 E0 00 00 00            mov eax, dword ptr [rsp + 0xe0]
00B9F187  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
00B9F18B  48 8B 84 24 D8 00 00 00         mov rax, qword ptr [rsp + 0xd8]
00B9F193  48 89 44 24 48                  mov qword ptr [rsp + 0x48], rax
00B9F198  48 8B 05 59 F9 45 00            mov rax, qword ptr [rip + 0x45f959]
00B9F19F  89 54 24 40                     mov dword ptr [rsp + 0x40], edx
00B9F1A3  41 8B D3                        mov edx, r11d
00B9F1A6  89 4C 24 38                     mov dword ptr [rsp + 0x38], ecx
00B9F1AA  8B 8C 24 C0 00 00 00            mov ecx, dword ptr [rsp + 0xc0]
00B9F1B1  89 4C 24 30                     mov dword ptr [rsp + 0x30], ecx
00B9F1B5  8B 8C 24 B8 00 00 00            mov ecx, dword ptr [rsp + 0xb8]
00B9F1BC  89 4C 24 28                     mov dword ptr [rsp + 0x28], ecx
00B9F1C0  48 8B 8C 24 B0 00 00 00         mov rcx, qword ptr [rsp + 0xb0]
00B9F1C8  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00B9F1CD  48 8B CB                        mov rcx, rbx
00B9F1D0  E8 FB B8 B1 FF                  call 0x1406baad0
00B9F1D5  48 81 C4 80 00 00 00            add rsp, 0x80
00B9F1DC  5B                              pop rbx
00B9F1DD  C3                              ret
00B9F1DE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall VerifierIoCreateFile(__int64 a1, int a2, __int64 a3, __int64 a4, __int64 a5, unsigned int a6, unsigned int a7, unsigned int a8, unsigned int a9, __int64 a10, unsigned int a11, unsigned int a12, __int64 a13, unsigned int a14)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned int v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned int v_stack_m48;
    unsigned int v_stack_m50;
    unsigned int v_stack_m58;
    unsigned int v_stack_m60;
    unsigned __int64 v_stack_m68;

    v_rsp = (v_rsp) - (128);
    v_stack_m20 = (unsigned int)((unsigned int)(a14));
    v_stack_m28 = a13;
    v_stack_m30 = (unsigned int)((unsigned int)(a12));
    v_stack_m38 = (unsigned int)((unsigned int)(a11));
    v_stack_m40 = a10;
    v_stack_m48 = (unsigned int)((unsigned int)(a9));
    v_stack_m50 = (unsigned int)((unsigned int)(a8));
    v_stack_m58 = (unsigned int)((unsigned int)(a7));
    v_stack_m60 = (unsigned int)((unsigned int)(a6));
    v_stack_m68 = a5;
    result = guard_dispatch_icall(a1, (unsigned int)((unsigned int)((unsigned int)(a2))), a3, a4);
    v_rsp = (v_rsp) + (128);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t VerifierIoCreateFile(int64_t Arg1, int32_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, uint32_t Arg6, uint32_t Arg7, uint32_t Arg8, uint32_t Arg9, int64_t Arg10, uint32_t Arg11, uint32_t Arg12, int64_t Arg13, uint32_t Arg14)
{
    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m20;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint32_t v_stack_m38;
    uint64_t v_stack_m40;
    uint32_t v_stack_m48;
    uint32_t v_stack_m50;
    uint32_t v_stack_m58;
    uint32_t v_stack_m60;
    uint64_t v_stack_m68;

    local_rsp = (local_rsp) - (128);
    v_stack_m20 = (uint32_t)((uint32_t)(Arg14));
    v_stack_m28 = Arg13;
    v_stack_m30 = (uint32_t)((uint32_t)(Arg12));
    v_stack_m38 = (uint32_t)((uint32_t)(Arg11));
    v_stack_m40 = Arg10;
    v_stack_m48 = (uint32_t)((uint32_t)(Arg9));
    v_stack_m50 = (uint32_t)((uint32_t)(Arg8));
    v_stack_m58 = (uint32_t)((uint32_t)(Arg7));
    v_stack_m60 = (uint32_t)((uint32_t)(Arg6));
    v_stack_m68 = Arg5;
    result = guard_dispatch_icall(Arg1, (uint32_t)((uint32_t)((uint32_t)(Arg2))), Arg3, Arg4);
    local_rsp = (local_rsp) + (128);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=pagevrfy&rva=0x00B9F140&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B9F140[BB_00B9F140]
  bb_00B9F1DE[BB_00B9F1DE]
```
