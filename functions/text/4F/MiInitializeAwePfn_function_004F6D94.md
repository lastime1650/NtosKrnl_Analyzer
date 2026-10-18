# MiInitializeAwePfn

- RVA: `0x004F6D94`–`0x004F6DE1` (길이 `77` bytes)
- VA: `0x00000001404F6D94`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `21`개 명령, `77/77` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004F6DC3` → [MiSetPfnIdentity](../2A/MiSetPfnIdentity_function_002A2350.md) (function, `0x002A2350`)
- `0x004F6DD5` → [MiSetPfnContainingFrame](../36/MiSetPfnContainingFrame_function_00363FC0.md) (function, `0x00363FC0`)

### Direct callers
- [MiInitializeMdlPfn](../2C/MiInitializeMdlPfn_function_002C9670.md) at `0x002C9736`
- [MiFillUserPhysicalMdl](../68/MiFillUserPhysicalMdl_function_006887D4.md) at `0x00688913`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004F6D94  40 53                           push rbx
004F6D96  48 83 EC 20                     sub rsp, 0x20
004F6D9A  48 C7 41 08 00 00 00 00         mov qword ptr [rcx + 8], 0
004F6DA2  BA 01 00 00 00                  mov edx, 1
004F6DA7  8B 41 20                        mov eax, dword ptr [rcx + 0x20]
004F6DAA  48 8B D9                        mov rbx, rcx
004F6DAD  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
004F6DB1  C1 E8 10                        shr eax, 0x10
004F6DB4  24 FE                           and al, 0xfe
004F6DB6  0C 06                           or al, 6
004F6DB8  88 44 24 32                     mov byte ptr [rsp + 0x32], al
004F6DBC  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
004F6DC0  89 41 20                        mov dword ptr [rcx + 0x20], eax
004F6DC3  E8 88 B5 DA FF                  call 0x1402a2350
004F6DC8  48 BA FE FF FF FF 3F 00 00 00   movabs rdx, 0x3ffffffffe
004F6DD2  48 8B CB                        mov rcx, rbx
004F6DD5  E8 E6 D1 E6 FF                  call 0x140363fc0
004F6DDA  48 83 C4 20                     add rsp, 0x20
004F6DDE  5B                              pop rbx
004F6DDF  C3                              ret
004F6DE0  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiInitializeAwePfn(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_p8;
    unsigned __int8 v_stack_pA;

    v_rsp = (v_rsp) - (32);
    *(unsigned __int64 *)(a1 + 8) = 0;
    v_stack_p8 = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 32)));
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 32))) >> (16));
    result = (unsigned __int8)((result) & (254));
    result = (unsigned __int8)((result) | (6));
    v_stack_pA = (unsigned __int8)(result);
    *(unsigned int *)(a1 + 32) = (unsigned int)((unsigned int)(v_stack_p8));
    result = MiSetPfnIdentity(a1, 1, a3, a4);
    result = MiSetPfnContainingFrame(a1, 1, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiInitializeAwePfn(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_p8;
    uint8_t v_stack_pA;

    local_rsp = (local_rsp) - (32);
    *(uint64_t *)(arg1 + 0x8) = 0;
    v_stack_p8 = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x20)));
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x20))) >> (16));
    result = (uint8_t)((result) & (254));
    result = (uint8_t)((result) | (6));
    v_stack_pA = (uint8_t)(result);
    *(uint32_t *)(arg1 + 0x20) = (uint32_t)((uint32_t)(v_stack_p8));
    result = MiSetPfnIdentity(Arg1, 1, a3, a4);
    result = MiSetPfnContainingFrame(Arg1, 1, a3, a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `W` |
| `Arg1` | `+ 0x20` | `32` | `R` |
| `Arg1` | `+ 0x20` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004F6D94&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004F6D94[BB_004F6D94]
  bb_004F6DE0[BB_004F6DE0]
```
