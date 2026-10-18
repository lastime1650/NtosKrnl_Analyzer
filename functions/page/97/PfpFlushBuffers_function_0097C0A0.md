# PfpFlushBuffers

- RVA: `0x0097C0A0`–`0x0097C0F8` (길이 `88` bytes)
- VA: `0x000000014097C0A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00096E38`
- 디코드: `23`개 명령, `88/88` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0097C0E8` → [PfpFlushEventBuffers](PfpFlushEventBuffers_function_0097BD4C.md) (function, `0x0097BD4C`)

### Direct callers
- [PfTLoggingWorker](PfTLoggingWorker_function_0097B140.md) at `0x0097B299`
- [PfTLoggingWorker](PfTLoggingWorker_function_0097B140.md) at `0x0097B346`
- [sub_00B29CFA](../B2/Unknown_function_00B29CFA.md) at `0x00B29CFD`
- [sub_00B29CFA](../B2/Unknown_function_00B29CFA.md) at `0x00B29D0B`

### Static image references
- `0x0097C0B3` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0097C0F2` → [sub_0097C3DE + 0x2D](Unknown_function_0097C3DE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0097C0A0  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
0097C0A5  55                              push rbp
0097C0A6  56                              push rsi
0097C0A7  57                              push rdi
0097C0A8  41 54                           push r12
0097C0AA  41 56                           push r14
0097C0AC  48 81 EC 90 00 00 00            sub rsp, 0x90
0097C0B3  48 8B 05 86 E6 48 00            mov rax, qword ptr [rip + 0x48e686]
0097C0BA  48 33 C4                        xor rax, rsp
0097C0BD  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0097C0C5  0F 57 C0                        xorps xmm0, xmm0
0097C0C8  33 F6                           xor esi, esi
0097C0CA  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
0097C0CF  C7 44 24 40 01 00 00 00         mov dword ptr [rsp + 0x40], 1
0097C0D7  4C 8B F1                        mov r14, rcx
0097C0DA  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
0097C0DF  8B DE                           mov ebx, esi
0097C0E1  48 89 74 24 30                  mov qword ptr [rsp + 0x30], rsi
0097C0E6  8B FE                           mov edi, esi
0097C0E8  E8 5F FC FF FF                  call 0x14097bd4c
0097C0ED  44 8B E0                        mov r12d, eax
0097C0F0  85 C0                           test eax, eax
0097C0F2  0F 88 13 03 00 00               js 0x14097c40b
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpFlushBuffers(__int64 a1)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_p20;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (144);
    result = (*(unsigned __int64 *)(v_rip + 4777606)) ^ (v_rsp);
    v_stack_m30 = result;
    v_rsi = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m78 = 1;
    v_stack_m70 = v_xmm0;
    v_stack_m88 = 0;
    result = PfpFlushEventBuffers(a1, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t PfpFlushBuffers(int64_t Arg1)
{
    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m30;
    uint64_t v_stack_m70;
    uint32_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_p20;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (144);
    result = (*(uint64_t *)(v_rip + 0x48E686)) ^ (local_rsp);
    v_stack_m30 = result;
    local_rsi = 0;
    v_stack_m80 = v_xmm0;
    v_stack_m78 = 1;
    v_stack_m70 = v_xmm0;
    v_stack_m88 = 0;
    result = PfpFlushEventBuffers(Arg1, a2, a3, a4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0097C0A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0097C0A0[BB_0097C0A0]
```
