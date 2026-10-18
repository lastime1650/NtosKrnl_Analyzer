# KeInitializeThreadedDpc

- RVA: `0x004FBED0`–`0x004FBEEA` (길이 `26` bytes)
- VA: `0x00000001404FBED0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `8`개 명령, `26/26` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [KiInitializeProcessor](../../pagelk/B6/KiInitializeProcessor_function_00B66A0C.md) at `0x00B66A7C`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004FBED0  33 C0                           xor eax, eax
004FBED2  C7 01 1A 01 00 00               mov dword ptr [rcx], 0x11a
004FBED8  48 89 41 38                     mov qword ptr [rcx + 0x38], rax
004FBEDC  48 89 41 10                     mov qword ptr [rcx + 0x10], rax
004FBEE0  48 89 51 18                     mov qword ptr [rcx + 0x18], rdx
004FBEE4  4C 89 41 20                     mov qword ptr [rcx + 0x20], r8
004FBEE8  C3                              ret
004FBEE9  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeInitializeThreadedDpc(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;

    result = 0;
    *(unsigned int *)(a1) = 282;
    *(unsigned __int64 *)(a1 + 56) = 0;
    *(unsigned __int64 *)(a1 + 16) = 0;
    *(unsigned __int64 *)(a1 + 24) = a2;
    *(unsigned __int64 *)(a1 + 32) = a3;
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KeInitializeThreadedDpc(void *ThreadedDpc, int64_t Arg2, int64_t Arg3)
{
    uint8_t *threadedDpc = (uint8_t *)ThreadedDpc;

    int64_t result;

    result = 0;
    *(uint32_t *)(threadedDpc) = 282;
    *(uint64_t *)(threadedDpc + 0x38) = 0;
    *(uint64_t *)(threadedDpc + 0x10) = 0;
    *(uint64_t *)(threadedDpc + 0x18) = Arg2;
    *(uint64_t *)(threadedDpc + 0x20) = Arg3;
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `ThreadedDpc` | `+ 0x0` | `32` | `W` |
| `ThreadedDpc` | `+ 0x10` | `64` | `W` |
| `ThreadedDpc` | `+ 0x18` | `64` | `W` |
| `ThreadedDpc` | `+ 0x20` | `64` | `W` |
| `ThreadedDpc` | `+ 0x38` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004FBED0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004FBED0[BB_004FBED0]
  bb_004FBEE9[BB_004FBEE9]
```
