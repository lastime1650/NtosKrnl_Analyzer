# sub_008B750F

- RVA: `0x008B750F`–`0x008B756E` (길이 `95` bytes)
- VA: `0x00000001408B750F`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00082B68`
- 디코드: `16`개 명령, `95/95` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x008B754F` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (function, `0x0020FF80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x008B7554` → RVA `0x00FD8010` (`PAGEDATA`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008B754F` → [PsReferencePrimaryTokenWithTag](../../text/20/PsReferencePrimaryTokenWithTag_function_0020FF80.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x008B753C` → [sub_008B76B1](Unknown_function_008B76B1.md) (`tail-transfer`)
  - `0x008B7568` → [sub_008B7711 + 0xB3](Unknown_function_008B7711.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
008B750F  4C 89 A4 24 78 02 00 00         mov qword ptr [rsp + 0x278], r12
008B7517  F3 0F 7F 44 24 70               movdqu xmmword ptr [rsp + 0x70], xmm0
008B751D  4C 8B A3 B8 00 00 00            mov r12, qword ptr [rbx + 0xb8]
008B7524  49 8B 84 24 D0 01 00 00         mov rax, qword ptr [r12 + 0x1d0]
008B752C  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
008B7534  8B 83 A0 05 00 00               mov eax, dword ptr [rbx + 0x5a0]
008B753A  A8 08                           test al, 8
008B753C  0F 85 6F 01 00 00               jne 0x1408b76b1
008B7542  BA 53 65 53 75                  mov edx, 0x75536553
008B7547  4C 89 6C 24 68                  mov qword ptr [rsp + 0x68], r13
008B754C  49 8B CC                        mov rcx, r12
008B754F  E8 2C 8A 95 FF                  call 0x14020ff80
008B7554  83 3D B5 0A 72 00 00            cmp dword ptr [rip + 0x720ab5], 0
008B755B  4C 8B A4 24 78 02 00 00         mov r12, qword ptr [rsp + 0x278]
008B7563  48 89 44 24 78                  mov qword ptr [rsp + 0x78], rax
008B7568  0F 85 56 02 00 00               jne 0x1408b77c4
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_008B750F(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25, __int64 a26, __int64 a27, __int64 a28, __int64 a29, __int64 a30, __int64 a31, __int64 a32, __int64 a33, __int64 a34, __int64 a35, __int64 a36, __int64 a37, __int64 a38, __int64 a39, __int64 a40, __int64 a41, __int64 a42, __int64 a43, __int64 a44, __int64 a45, __int64 a46, __int64 a47, __int64 a48, __int64 a49, __int64 a50, __int64 a51, __int64 a52, __int64 a53, __int64 a54, __int64 a55, __int64 a56, __int64 a57, __int64 a58, __int64 a59, __int64 a60, __int64 a61, __int64 a62, __int64 a63, __int64 a64, __int64 a65, __int64 a66, __int64 a67, __int64 a68, __int64 a69, __int64 a70, __int64 a71, __int64 a72, __int64 a73, __int64 a74, __int64 a75, __int64 a76, __int64 a77, __int64 a78, __int64 a79)
{
    __int64 result;
    unsigned __int64 v_stack_p278;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p80;

    v_stack_p278 = v_r12;
    v_stack_p70 = v_xmm0;
    v_stack_p80 = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rbx + 184) + 464);
    v_stack_p68 = v_r13;
    result = PsReferencePrimaryTokenWithTag(*(unsigned __int64 *)(v_rbx + 184), (unsigned int)(0x75536553ULL), a3, a4);
    v_stack_p78 = result;
}
```

## 5. (Beta) C Style

```c
int64_t sub_008B750F(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, uint64_t Arg16, uint64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, uint64_t Arg24, uint64_t Arg25, uint64_t Arg26, uint64_t Arg27, uint64_t Arg28, uint64_t Arg29, uint64_t Arg30, uint64_t Arg31, uint64_t Arg32, uint64_t Arg33, uint64_t Arg34, uint64_t Arg35, uint64_t Arg36, uint64_t Arg37, uint64_t Arg38, uint64_t Arg39, uint64_t Arg40, uint64_t Arg41, uint64_t Arg42, uint64_t Arg43, uint64_t Arg44, uint64_t Arg45, uint64_t Arg46, uint64_t Arg47, uint64_t Arg48, uint64_t Arg49, uint64_t Arg50, uint64_t Arg51, uint64_t Arg52, uint64_t Arg53, uint64_t Arg54, uint64_t Arg55, uint64_t Arg56, uint64_t Arg57, uint64_t Arg58, uint64_t Arg59, uint64_t Arg60, uint64_t Arg61, uint64_t Arg62, uint64_t Arg63, uint64_t Arg64, uint64_t Arg65, uint64_t Arg66, uint64_t Arg67, uint64_t Arg68, uint64_t Arg69, uint64_t Arg70, uint64_t Arg71, uint64_t Arg72, uint64_t Arg73, uint64_t Arg74, uint64_t Arg75, uint64_t Arg76, uint64_t Arg77, uint64_t Arg78, int64_t Arg79)
{
    int64_t result;
    uint64_t v_stack_p278;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p80;

    v_stack_p278 = local_r12;
    v_stack_p70 = v_xmm0;
    v_stack_p80 = *(uint64_t *)(*(uint64_t *)(local_rbx + 0xB8) + 0x1D0);
    v_stack_p68 = local_r13;
    result = PsReferencePrimaryTokenWithTag(*(uint64_t *)(local_rbx + 0xB8), (uint32_t)(0x75536553ULL), Arg3, Arg4);
    v_stack_p78 = result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008B750F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008B750F[BB_008B750F]
  bb_008B7542[BB_008B7542]
  bb_008B750F -->|fallthrough| bb_008B7542
```
