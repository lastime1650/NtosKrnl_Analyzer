# MiZeroThreadContextSetExiting

- RVA: `0x002CC590`–`0x002CC5CC` (길이 `60` bytes)
- VA: `0x00000001402CC590`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `16`개 명령, `60/60` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002CC5B1` → [MiSetZeroPageThreadPriority](../31/MiSetZeroPageThreadPriority_function_0031E620.md) (function, `0x0031E620`)

### Direct callers
- [MiBackgroundZeroNodePages](MiBackgroundZeroNodePages_function_002CB9B0.md) at `0x002CBB17`
- [MiBackgroundZeroNodePages](MiBackgroundZeroNodePages_function_002CB9B0.md) at `0x002CBB42`
- [MiBackgroundZeroLocalPages](../31/MiBackgroundZeroLocalPages_function_0031EF30.md) at `0x0031F514`
- [MiBackgroundZeroLocalPages](../31/MiBackgroundZeroLocalPages_function_0031EF30.md) at `0x0031F7E6`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002CC590  40 53                           push rbx
002CC592  48 83 EC 20                     sub rsp, 0x20
002CC596  8B 81 80 01 00 00               mov eax, dword ptr [rcx + 0x180]
002CC59C  BA 0C 00 00 00                  mov edx, 0xc
002CC5A1  83 C8 04                        or eax, 4
002CC5A4  48 8B D9                        mov rbx, rcx
002CC5A7  89 81 80 01 00 00               mov dword ptr [rcx + 0x180], eax
002CC5AD  44 8D 42 F5                     lea r8d, [rdx - 0xb]
002CC5B1  E8 6A 20 05 00                  call 0x14031e620
002CC5B6  8B 83 80 01 00 00               mov eax, dword ptr [rbx + 0x180]
002CC5BC  83 C8 08                        or eax, 8
002CC5BF  89 83 80 01 00 00               mov dword ptr [rbx + 0x180], eax
002CC5C5  48 83 C4 20                     add rsp, 0x20
002CC5C9  5B                              pop rbx
002CC5CA  C3                              ret
002CC5CB  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiZeroThreadContextSetExiting(__int64 a1)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 384))) | (4));
    *(unsigned int *)(a1 + 384) = (unsigned int)(result);
    result = MiSetZeroPageThreadPriority(a1, 12, 12 - 11, a4);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a1 + 384))) | (8));
    *(unsigned int *)(a1 + 384) = (unsigned int)(result);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiZeroThreadContextSetExiting(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x180))) | (4));
    *(uint32_t *)(arg1 + 0x180) = (uint32_t)(result);
    result = MiSetZeroPageThreadPriority(Arg1, 12, 12 - 11, a4);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(arg1 + 0x180))) | (8));
    *(uint32_t *)(arg1 + 0x180) = (uint32_t)(result);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x180` | `32` | `R` |
| `Arg1` | `+ 0x180` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002CC590&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002CC590[BB_002CC590]
  bb_002CC5CB[BB_002CC5CB]
```
