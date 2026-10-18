# sub_0099FA2D

- RVA: `0x0099FA2D`–`0x0099FAAF` (길이 `130` bytes)
- VA: `0x000000014099FA2D`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009B220`
- 디코드: `28`개 명령, `130/130` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **5**

### Outgoing calls
- `0x0099FA43` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (function, `0x00210230`)
- `0x0099FA75` → [ExpAcquireFastMutexContended](../../text/45/ExpAcquireFastMutexContended_function_00450288.md) (function, `0x00450288`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0099FA32` → RVA `0x00EF5880` (`.data`; read)
- `0x0099FA53` → RVA `0x00FC6D20` (`ALMOSTRO`; read)
- `0x0099FA60` → RVA `0x00EF5880` (`.data`; read/write)
- `0x0099FA91` → RVA `0x00EF5888` (`.data`; write)
- `0x0099FAA1` → RVA `0x00EF58B0` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0099FA43` → [KeAbPreAcquire](../../text/21/KeAbPreAcquire_function_00210230.md) (`PAGE` → `.text`)
  - `0x0099FA75` → [ExpAcquireFastMutexContended](../../text/45/ExpAcquireFastMutexContended_function_00450288.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x0099FA5A` → [sub_0099FB10](Unknown_function_0099FB10.md) (`tail-transfer`)
  - `0x0099FAAD` → [sub_0099FAAF + 0x48](Unknown_function_0099FAAF.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0099FA2D  48 89 74 24 50                  mov qword ptr [rsp + 0x50], rsi
0099FA32  48 8D 0D 47 5E 55 00            lea rcx, [rip + 0x555e47]
0099FA39  45 33 C0                        xor r8d, r8d
0099FA3C  48 89 7C 24 58                  mov qword ptr [rsp + 0x58], rdi
0099FA41  33 D2                           xor edx, edx
0099FA43  E8 E8 07 87 FF                  call 0x140210230
0099FA48  48 8B F8                        mov rdi, rax
0099FA4B  44 0F 20 C6                     mov rsi, cr8
0099FA4F  44 0F 22 C5                     mov cr8, rbp
0099FA53  83 3D C6 72 62 00 00            cmp dword ptr [rip + 0x6272c6], 0
0099FA5A  0F 85 B0 00 00 00               jne 0x14099fb10
0099FA60  F0 0F BA 35 17 5E 55 00 00      lock btr dword ptr [rip + 0x555e17], 0
0099FA69  72 0F                           jb 0x14099fa7a
0099FA6B  48 8B D7                        mov rdx, rdi
0099FA6E  48 8D 0D 0B 5E 55 00            lea rcx, [rip + 0x555e0b]
0099FA75  E8 0E 08 AB FF                  call 0x140450288
0099FA7A  48 85 FF                        test rdi, rdi
0099FA7D  74 04                           je 0x14099fa83
0099FA7F  40 88 6F 0A                     mov byte ptr [rdi + 0xa], bpl
0099FA83  65 48 8B 04 25 88 01 00 00      mov rax, qword ptr gs:[0x188]
0099FA8C  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
0099FA91  48 89 05 F0 5D 55 00            mov qword ptr [rip + 0x555df0], rax
0099FA98  40 0F B6 C6                     movzx eax, sil
0099FA9C  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
0099FAA1  89 05 09 5E 55 00               mov dword ptr [rip + 0x555e09], eax
0099FAA7  0F B6 43 40                     movzx eax, byte ptr [rbx + 0x40]
0099FAAB  A8 02                           test al, 2
0099FAAD  74 48                           je 0x14099faf7
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_0099FA2D(__int64 a1, int a2, int a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_p58;

    v_stack_p50 = v_rsi;
    a3 = 0;
    v_stack_p58 = v_rdi;
    a2 = 0;
    result = KeAbPreAcquire(v_rip + 5594695, a2, a3, a4);
    if ((*(unsigned int *)(v_rip + 6451910)) >= 0) {
        a2 = result;
        a1 = v_rip + 5594635;
        result = ExpAcquireFastMutexContended(a1, a2, a3, a4);
    }
    if (result != 0) {
        *(unsigned __int8 *)(result + 10) = (unsigned __int8)(v_rbp);
    }
    *(unsigned __int64 *)(v_rip + 5594608) = *(unsigned __int64 *)(gs_base + (0 + 392));
    *(unsigned int *)(v_rip + 5594633) = (unsigned int)((unsigned __int8)(v_cr8));
}
```

## 5. (Beta) C Style

```c
int64_t sub_0099FA2D(int64_t Arg1, int32_t Arg2, int32_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, int64_t Arg10, int64_t Arg11)
{
    int64_t result;
    uint64_t v_stack_p50;
    uint64_t v_stack_p58;

    v_stack_p50 = local_rsi;
    Arg3 = 0;
    v_stack_p58 = local_rdi;
    Arg2 = 0;
    result = KeAbPreAcquire(v_rip + 5594695, Arg2, Arg3, Arg4);
    if ((*(uint32_t *)(v_rip + 0x6272C6)) >= 0) {
        Arg2 = result;
        Arg1 = v_rip + 5594635;
        result = ExpAcquireFastMutexContended(Arg1, Arg2, Arg3, Arg4);
    }
    if (result != 0) {
        *(uint8_t *)(result + 0xA) = (uint8_t)(local_rbp);
    }
    *(uint64_t *)(v_rip + 0x555DF0) = *(uint64_t *)(gs_base + (0 + 0x188));
    *(uint32_t *)(v_rip + 0x555E09) = (uint32_t)((uint8_t)(v_cr8));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0099FA2D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0099FA2D[BB_0099FA2D]
  bb_0099FA60[BB_0099FA60]
  bb_0099FA6B[BB_0099FA6B]
  bb_0099FA7A[BB_0099FA7A]
  bb_0099FA7F[BB_0099FA7F]
  bb_0099FA83[BB_0099FA83]
  bb_0099FA2D -->|fallthrough| bb_0099FA60
  bb_0099FA60 -->|branch| bb_0099FA7A
  bb_0099FA60 -->|fallthrough| bb_0099FA6B
  bb_0099FA6B -->|flow| bb_0099FA7A
  bb_0099FA7A -->|branch| bb_0099FA83
  bb_0099FA7A -->|fallthrough| bb_0099FA7F
  bb_0099FA7F -->|flow| bb_0099FA83
```
