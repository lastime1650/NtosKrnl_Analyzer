# KeInitializeSemaphore

- RVA: `0x004660D0`–`0x004660EB` (길이 `27` bytes)
- VA: `0x00000001404660D0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `9`개 명령, `27/27` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [PopFxInitializeWorkPool](../../page/75/PopFxInitializeWorkPool_function_00759290.md) at `0x007592DD`
- [NtCreateSemaphore](../../page/8C/NtCreateSemaphore_function_008C38D0.md) at `0x008C3ABE`
- [AlpcpInitializePort](../../page/92/AlpcpInitializePort_function_00925DC4.md) at `0x00925EC2`
- [PspAllocateThread](../../page/9E/PspAllocateThread_function_009EF72C.md) at `0x009EFB59`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004660D0  48 8D 41 08                     lea rax, [rcx + 8]
004660D4  C6 01 05                        mov byte ptr [rcx], 5
004660D7  C6 41 02 08                     mov byte ptr [rcx + 2], 8
004660DB  89 51 04                        mov dword ptr [rcx + 4], edx
004660DE  48 89 40 08                     mov qword ptr [rax + 8], rax
004660E2  48 89 00                        mov qword ptr [rax], rax
004660E5  44 89 41 18                     mov dword ptr [rcx + 0x18], r8d
004660E9  C3                              ret
004660EA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KeInitializeSemaphore(__int64 a1, int a2, int a3)
{
    *(unsigned __int8 *)(a1) = 5;
    *(unsigned __int8 *)(a1 + 2) = 8;
    *(unsigned int *)(a1 + 4) = a2;
    *(unsigned __int64 *)(a1 + 8 + 8) = a1 + 8;
    *(unsigned __int64 *)(a1 + 8) = a1 + 8;
    *(unsigned int *)(a1 + 24) = a3;
    return a1 + 8;
}
```

## 5. (Beta) C Style

```c
void *KeInitializeSemaphore(void *Semaphore, int32_t Arg2, int32_t Arg3)
{
    uint8_t *semaphore = (uint8_t *)Semaphore;

    *(uint8_t *)(semaphore) = 5;
    *(uint8_t *)(semaphore + 0x2) = 8;
    *(uint32_t *)(semaphore + 0x4) = Arg2;
    *(void **)(semaphore + 0x8 + 0x8) = Semaphore + 8;
    *(void **)(semaphore + 0x8) = Semaphore + 8;
    *(uint32_t *)(semaphore + 0x18) = Arg3;
    return Semaphore + 8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Semaphore` | `+ 0x0` | `8` | `W` |
| `Semaphore` | `+ 0x0` | `64` | `W` |
| `Semaphore` | `+ 0x2` | `8` | `W` |
| `Semaphore` | `+ 0x4` | `32` | `W` |
| `Semaphore` | `+ 0x8` | `64` | `R` |
| `Semaphore` | `+ 0x8` | `64` | `W` |
| `Semaphore` | `+ 0x18` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004660D0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004660D0[BB_004660D0]
  bb_004660EA[BB_004660EA]
```
