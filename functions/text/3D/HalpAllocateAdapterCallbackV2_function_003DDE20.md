# HalpAllocateAdapterCallbackV2

- RVA: `0x003DDE20`–`0x003DDEB6` (길이 `150` bytes)
- VA: `0x00000001403DDE20`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00094444`
- 디코드: `34`개 명령, `150/150` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [sub_003DD362](Unknown_function_003DD362.md) at `0x003DD4F5`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x003DDEB0` → [sub_003DE131](Unknown_function_003DE131.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003DDE20  4C 89 44 24 18                  mov qword ptr [rsp + 0x18], r8
003DDE25  48 89 4C 24 08                  mov qword ptr [rsp + 8], rcx
003DDE2A  53                              push rbx
003DDE2B  55                              push rbp
003DDE2C  56                              push rsi
003DDE2D  57                              push rdi
003DDE2E  41 54                           push r12
003DDE30  41 55                           push r13
003DDE32  48 81 EC D8 00 00 00            sub rsp, 0xd8
003DDE39  49 8B 71 08                     mov rsi, qword ptr [r9 + 8]
003DDE3D  4D 8D 69 30                     lea r13, [r9 + 0x30]
003DDE41  41 0F B6 81 98 00 00 00         movzx eax, byte ptr [r9 + 0x98]
003DDE49  49 8D 7D 10                     lea rdi, [r13 + 0x10]
003DDE4D  49 8B 51 20                     mov rdx, qword ptr [r9 + 0x20]
003DDE51  4C 8B D1                        mov r10, rcx
003DDE54  4D 8B 59 78                     mov r11, qword ptr [r9 + 0x78]
003DDE58  49 8B 59 68                     mov rbx, qword ptr [r9 + 0x68]
003DDE5C  45 8B 61 28                     mov r12d, dword ptr [r9 + 0x28]
003DDE60  49 8B A9 90 00 00 00            mov rbp, qword ptr [r9 + 0x90]
003DDE67  4D 89 41 18                     mov qword ptr [r9 + 0x18], r8
003DDE6B  4D 8B 81 80 00 00 00            mov r8, qword ptr [r9 + 0x80]
003DDE72  88 84 24 28 01 00 00            mov byte ptr [rsp + 0x128], al
003DDE79  4D 89 4D 08                     mov qword ptr [r13 + 8], r9
003DDE7D  8B 46 2C                        mov eax, dword ptr [rsi + 0x2c]
003DDE80  03 46 28                        add eax, dword ptr [rsi + 0x28]
003DDE83  2B C2                           sub eax, edx
003DDE85  4C 89 9C 24 88 00 00 00         mov qword ptr [rsp + 0x88], r11
003DDE8D  03 46 20                        add eax, dword ptr [rsi + 0x20]
003DDE90  4C 89 84 24 90 00 00 00         mov qword ptr [rsp + 0x90], r8
003DDE98  48 89 9C 24 98 00 00 00         mov qword ptr [rsp + 0x98], rbx
003DDEA0  4C 89 AC 24 80 00 00 00         mov qword ptr [rsp + 0x80], r13
003DDEA8  48 89 54 24 50                  mov qword ptr [rsp + 0x50], rdx
003DDEAD  45 85 E4                        test r12d, r12d
003DDEB0  0F 84 7B 02 00 00               je 0x1403de131
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall HalpAllocateAdapterCallbackV2(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_mB8;
    unsigned __int64 v_stack_p18;
    unsigned __int8 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p18 = a3;
    v_stack_p8 = a1;
    v_rsp = (v_rsp) - (216);
    *(unsigned __int64 *)(a4 + 24) = a3;
    v_stack_p20 = (unsigned __int8)(*(unsigned __int8 *)(a4 + 152));
    *(unsigned __int64 *)(a4 + 48 + 8) = a4;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a4 + 8) + 44))) + (*(unsigned int *)(*(unsigned __int64 *)(a4 + 8) + 40)));
    result = (unsigned int)((result) - ((unsigned int)(*(unsigned __int64 *)(a4 + 32))));
    v_stack_m80 = *(unsigned __int64 *)(a4 + 120);
    result = (unsigned int)((result) + (*(unsigned int *)(*(unsigned __int64 *)(a4 + 8) + 32)));
    v_stack_m78 = *(unsigned __int64 *)(a4 + 128);
    v_stack_m70 = *(unsigned __int64 *)(a4 + 104);
    v_stack_m88 = a4 + 48;
    v_stack_mB8 = *(unsigned __int64 *)(a4 + 32);
}
```

## 5. (Beta) C Style

```c
int64_t HalpAllocateAdapterCallbackV2(int64_t Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_mB8;
    uint64_t v_stack_p18;
    uint8_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p18 = Arg3;
    v_stack_p8 = Arg1;
    local_rsp = (local_rsp) - (216);
    *(uint64_t *)(arg4 + 0x18) = Arg3;
    v_stack_p20 = (uint8_t)(*(uint8_t *)(arg4 + 0x98));
    *(void **)(arg4 + 0x30 + 0x8) = Arg4;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg4 + 0x8) + 0x2C))) + (*(uint32_t *)(*(uint64_t *)(arg4 + 0x8) + 0x28)));
    result = (uint32_t)((result) - ((uint32_t)(*(uint64_t *)(arg4 + 0x20))));
    v_stack_m80 = *(uint64_t *)(arg4 + 0x78);
    result = (uint32_t)((result) + (*(uint32_t *)(*(uint64_t *)(arg4 + 0x8) + 0x20)));
    v_stack_m78 = *(uint64_t *)(arg4 + 0x80);
    v_stack_m70 = *(uint64_t *)(arg4 + 0x68);
    v_stack_m88 = Arg4 + 48;
    v_stack_mB8 = *(uint64_t *)(arg4 + 0x20);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg4` | `+ 0x8` | `64` | `R` |
| `Arg4` | `+ 0x8` | `64` | `W` |
| `Arg4` | `+ 0x10` | `64` | `R` |
| `Arg4` | `+ 0x18` | `64` | `W` |
| `Arg4` | `+ 0x20` | `64` | `R` |
| `Arg4` | `+ 0x28` | `32` | `R` |
| `Arg4` | `+ 0x30` | `64` | `R` |
| `Arg4` | `+ 0x68` | `64` | `R` |
| `Arg4` | `+ 0x78` | `64` | `R` |
| `Arg4` | `+ 0x80` | `64` | `R` |
| `Arg4` | `+ 0x90` | `64` | `R` |
| `Arg4` | `+ 0x98` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003DDE20&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003DDE20[BB_003DDE20]
```
