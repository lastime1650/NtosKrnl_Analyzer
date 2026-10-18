# MiLockMultipleZeroChunks

- RVA: `0x0031F860`–`0x0031F8A6` (길이 `70` bytes)
- VA: `0x000000014031F860`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00075364`
- 디코드: `20`개 명령, `70/70` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiBackgroundZeroLocalPages](MiBackgroundZeroLocalPages_function_0031EF30.md) at `0x0031F375`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0031F8A0` → [sub_0031F9C0](Unknown_function_0031F9C0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0031F860  40 53                           push rbx
0031F862  55                              push rbp
0031F863  56                              push rsi
0031F864  57                              push rdi
0031F865  41 55                           push r13
0031F867  48 83 EC 40                     sub rsp, 0x40
0031F86B  48 8B D9                        mov rbx, rcx
0031F86E  33 FF                           xor edi, edi
0031F870  8B 49 0C                        mov ecx, dword ptr [rcx + 0xc]
0031F873  89 4C 24 70                     mov dword ptr [rsp + 0x70], ecx
0031F877  8B 43 10                        mov eax, dword ptr [rbx + 0x10]
0031F87A  48 8B 73 40                     mov rsi, qword ptr [rbx + 0x40]
0031F87E  48 8B 53 28                     mov rdx, qword ptr [rbx + 0x28]
0031F882  4C 8B 6B 38                     mov r13, qword ptr [rbx + 0x38]
0031F886  48 69 E8 80 DF 00 00            imul rbp, rax, 0xdf80
0031F88D  48 8B 43 20                     mov rax, qword ptr [rbx + 0x20]
0031F891  48 89 54 24 78                  mov qword ptr [rsp + 0x78], rdx
0031F896  48 03 68 10                     add rbp, qword ptr [rax + 0x10]
0031F89A  39 BE 18 01 00 00               cmp dword ptr [rsi + 0x118], edi
0031F8A0  0F 86 1A 01 00 00               jbe 0x14031f9c0
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiLockMultipleZeroChunks(__int64 a1)
{
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p8;

    v_rsp = (v_rsp) - (64);
    v_rdi = 0;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12)));
    v_rbp = (v_rbp) * ((unsigned int)(*(unsigned int *)(a1 + 16)));
    v_stack_p10 = *(unsigned __int64 *)(a1 + 40);
    v_rbp = (v_rbp) + (*(unsigned __int64 *)(*(unsigned __int64 *)(a1 + 32) + 16));
}
```

## 5. (Beta) C Style

```c
int64_t MiLockMultipleZeroChunks(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint32_t v_stack_p8;

    local_rsp = (local_rsp) - (64);
    local_rdi = 0;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC)));
    local_rbp = (local_rbp) * ((uint32_t)(*(uint32_t *)(arg1 + 0x10)));
    v_stack_p10 = *(uint64_t *)(arg1 + 0x28);
    local_rbp = (local_rbp) + (*(uint64_t *)(*(uint64_t *)(arg1 + 0x20) + 0x10));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x10` | `32` | `R` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `R` |
| `Arg1` | `+ 0x38` | `64` | `R` |
| `Arg1` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0031F860&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0031F860[BB_0031F860]
```
