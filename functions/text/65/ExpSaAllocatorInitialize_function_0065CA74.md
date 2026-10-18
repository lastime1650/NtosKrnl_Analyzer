# ExpSaAllocatorInitialize

- RVA: `0x0065CA74`–`0x0065CAD3` (길이 `95` bytes)
- VA: `0x000000014065CA74`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `28`개 명령, `95/95` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0065CA89` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [ExpSaInitialize](ExpSaInitialize_function_0065CADC.md) at `0x0065CC62`
- [ExpSaInitialize](ExpSaInitialize_function_0065CADC.md) at `0x0065CC88`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0065CA74  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0065CA79  57                              push rdi
0065CA7A  48 83 EC 20                     sub rsp, 0x20
0065CA7E  8B DA                           mov ebx, edx
0065CA80  48 8B F9                        mov rdi, rcx
0065CA83  33 D2                           xor edx, edx
0065CA85  44 8D 42 48                     lea r8d, [rdx + 0x48]
0065CA89  E8 B2 A1 06 00                  call 0x1406c6c40
0065CA8E  F6 C3 01                        test bl, 1
0065CA91  74 07                           je 0x14065ca9a
0065CA93  C7 47 40 01 00 00 00            mov dword ptr [rdi + 0x40], 1
0065CA9A  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0065CA9F  48 8D 47 08                     lea rax, [rdi + 8]
0065CAA3  48 89 40 08                     mov qword ptr [rax + 8], rax
0065CAA7  48 89 00                        mov qword ptr [rax], rax
0065CAAA  48 8D 47 18                     lea rax, [rdi + 0x18]
0065CAAE  48 89 40 08                     mov qword ptr [rax + 8], rax
0065CAB2  48 89 00                        mov qword ptr [rax], rax
0065CAB5  33 C0                           xor eax, eax
0065CAB7  48 89 07                        mov qword ptr [rdi], rax
0065CABA  48 89 47 28                     mov qword ptr [rdi + 0x28], rax
0065CABE  89 47 30                        mov dword ptr [rdi + 0x30], eax
0065CAC1  48 89 47 38                     mov qword ptr [rdi + 0x38], rax
0065CAC5  C7 47 34 04 00 00 00            mov dword ptr [rdi + 0x34], 4
0065CACC  48 83 C4 20                     add rsp, 0x20
0065CAD0  5F                              pop rdi
0065CAD1  C3                              ret
0065CAD2  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExpSaAllocatorInitialize(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    a2 = 0;
    result = memset(a1, a2, a2 + 72, a4);
    if ((((unsigned __int8)((unsigned int)(a2))) & (1)) != 0) {
        *(unsigned int *)(a1 + 64) = 1;
    }
    *(unsigned __int64 *)(a1 + 8 + 8) = a1 + 8;
    *(unsigned __int64 *)(a1 + 8) = a1 + 8;
    *(unsigned __int64 *)(a1 + 24 + 8) = a1 + 24;
    *(unsigned __int64 *)(a1 + 24) = a1 + 24;
    result = 0;
    *(unsigned __int64 *)(a1) = 0;
    *(unsigned __int64 *)(a1 + 40) = 0;
    *(unsigned int *)(a1 + 48) = 0;
    *(unsigned __int64 *)(a1 + 56) = 0;
    *(unsigned int *)(a1 + 52) = 4;
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExpSaAllocatorInitialize(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    Arg2 = 0;
    result = memset(Arg1, Arg2, Arg2 + 72, a4);
    if ((((uint8_t)((uint32_t)(Arg2))) & (1)) != 0) {
        *(uint32_t *)(arg1 + 0x40) = 1;
    }
    *(void **)(arg1 + 0x8 + 0x8) = Arg1 + 8;
    *(void **)(arg1 + 0x8) = Arg1 + 8;
    *(void **)(arg1 + 0x18 + 0x8) = Arg1 + 24;
    *(void **)(arg1 + 0x18) = Arg1 + 24;
    result = 0;
    *(uint64_t *)(arg1) = 0;
    *(uint64_t *)(arg1 + 0x28) = 0;
    *(uint32_t *)(arg1 + 0x30) = 0;
    *(uint64_t *)(arg1 + 0x38) = 0;
    *(uint32_t *)(arg1 + 0x34) = 4;
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `W` |
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x18` | `64` | `R` |
| `Arg1` | `+ 0x28` | `64` | `W` |
| `Arg1` | `+ 0x30` | `32` | `W` |
| `Arg1` | `+ 0x34` | `32` | `W` |
| `Arg1` | `+ 0x38` | `64` | `W` |
| `Arg1` | `+ 0x40` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0065CA74&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0065CA74[BB_0065CA74]
  bb_0065CA93[BB_0065CA93]
  bb_0065CA9A[BB_0065CA9A]
  bb_0065CAD2[BB_0065CAD2]
  bb_0065CA74 -->|branch| bb_0065CA9A
  bb_0065CA74 -->|fallthrough| bb_0065CA93
  bb_0065CA93 -->|flow| bb_0065CA9A
```
