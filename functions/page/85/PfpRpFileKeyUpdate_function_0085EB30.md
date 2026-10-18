# PfpRpFileKeyUpdate

- RVA: `0x0085EB30`–`0x0085EB76` (길이 `70` bytes)
- VA: `0x000000014085EB30`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006B24C`
- 디코드: `19`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_00342822](../../text/34/Unknown_function_00342822.md) at `0x0034286B`
- [sub_00342822](../../text/34/Unknown_function_00342822.md) at `0x003428DA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0085EB70` → [sub_0085F08A](Unknown_function_0085F08A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0085EB30  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
0085EB35  53                              push rbx
0085EB36  56                              push rsi
0085EB37  57                              push rdi
0085EB38  41 54                           push r12
0085EB3A  41 57                           push r15
0085EB3C  48 81 EC 80 00 00 00            sub rsp, 0x80
0085EB43  48 8B 42 10                     mov rax, qword ptr [rdx + 0x10]
0085EB47  45 33 FF                        xor r15d, r15d
0085EB4A  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0085EB4F  41 8B D8                        mov ebx, r8d
0085EB52  8B 81 98 00 00 00               mov eax, dword ptr [rcx + 0x98]
0085EB58  48 8B F2                        mov rsi, rdx
0085EB5B  4C 89 7C 24 38                  mov qword ptr [rsp + 0x38], r15
0085EB60  4C 8B E1                        mov r12, rcx
0085EB63  44 89 BC 24 C8 00 00 00         mov dword ptr [rsp + 0xc8], r15d
0085EB6B  41 8B FF                        mov edi, r15d
0085EB6E  A8 01                           test al, 1
0085EB70  0F 84 14 05 00 00               je 0x14085f08a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PfpRpFileKeyUpdate(__int64 a1, __int64 a2, int a3)
{
    __int64 v_r15;
    __int64 v_rsp;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m88;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (128);
    v_r15 = 0;
    v_stack_m88 = *(unsigned __int64 *)(a2 + 16);
    v_stack_m70 = 0;
    v_stack_p20 = 0;
}
```

## 5. (Beta) C Style

```c
int64_t PfpRpFileKeyUpdate(void *Arg1, void *Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t local_r15;
    int64_t local_rsp;
    uint64_t v_stack_m70;
    uint64_t v_stack_m88;
    uint32_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (128);
    local_r15 = 0;
    v_stack_m88 = *(uint64_t *)(arg2 + 0x10);
    v_stack_m70 = 0;
    v_stack_p20 = 0;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x98` | `32` | `R` |
| `Arg2` | `+ 0x10` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0085EB30&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0085EB30[BB_0085EB30]
```
