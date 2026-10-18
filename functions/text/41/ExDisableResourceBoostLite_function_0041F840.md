# ExDisableResourceBoostLite

- RVA: `0x0041F840`–`0x0041F89B` (길이 `91` bytes)
- VA: `0x000000014041F840`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071A74`
- 디코드: `26`개 명령, `91/91` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **3**; 고유 호출 대상: **3**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0041F871` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)
- `0x0041F880` → [KeAcquireInStackQueuedSpinLock](../27/KeAcquireInStackQueuedSpinLock_function_002757A0.md) (function, `0x002757A0`)
- `0x0041F88F` → [KeReleaseInStackQueuedSpinLock](../34/KeReleaseInStackQueuedSpinLock_function_00342CE0.md) (function, `0x00342CE0`)

### Direct callers
- [CcPinFileData](../33/CcPinFileData_function_0033FB40.md) at `0x00340302`
- [CcAllocateInitializeBcb](CcAllocateInitializeBcb_function_0041F5A4.md) at `0x0041F6D9`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0041F840  40 53                           push rbx
0041F842  48 83 EC 50                     sub rsp, 0x50
0041F846  33 C0                           xor eax, eax
0041F848  0F 57 C0                        xorps xmm0, xmm0
0041F84B  F6 41 1A 01                     test byte ptr [rcx + 0x1a], 1
0041F84F  48 8B D9                        mov rbx, rcx
0041F852  0F 11 44 24 30                  movups xmmword ptr [rsp + 0x30], xmm0
0041F857  48 89 44 24 40                  mov qword ptr [rsp + 0x40], rax
0041F85C  74 19                           je 0x14041f877
0041F85E  48 21 44 24 20                  and qword ptr [rsp + 0x20], rax
0041F863  8D 50 0E                        lea edx, [rax + 0xe]
0041F866  4C 8B C1                        mov r8, rcx
0041F869  45 33 C9                        xor r9d, r9d
0041F86C  B9 C6 01 00 00                  mov ecx, 0x1c6
0041F871  E8 EA DD 0D 00                  call 0x1404fd660
0041F876  CC                              int3
0041F877  48 83 C1 60                     add rcx, 0x60
0041F87B  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
0041F880  E8 1B 5F E5 FF                  call 0x1402757a0
0041F885  66 83 4B 1A 08                  or word ptr [rbx + 0x1a], 8
0041F88A  48 8D 4C 24 30                  lea rcx, [rsp + 0x30]
0041F88F  E8 4C 34 F2 FF                  call 0x140342ce0
0041F894  48 83 C4 50                     add rsp, 0x50
0041F898  5B                              pop rbx
0041F899  C3                              ret
0041F89A  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ExDisableResourceBoostLite(__int64 a1, __int64 a2, __int64 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;

    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m28 = v_xmm0;
    v_stack_m18 = 0;
    if (((*(unsigned __int8 *)(a1 + 26)) & (1)) != 0) {
        a2 = result + 14;
        a3 = a1;
        a4 = 0;
        a1 = 454;
        result = KeBugCheckEx(a1, a2, a3, a4);
    }
    a1 = (a1) + (96);
    result = KeAcquireInStackQueuedSpinLock(a1, v_stack_m28, a3, a4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m28, v_stack_m28, a3, a4);
    v_rsp = (v_rsp) + (80);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t ExDisableResourceBoostLite(void *Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;

    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m28 = v_xmm0;
    v_stack_m18 = 0;
    if (((*(uint8_t *)(arg1 + 0x1A)) & (1)) != 0) {
        Arg2 = result + 14;
        Arg3 = Arg1;
        Arg4 = 0;
        Arg1 = 454;
        result = KeBugCheckEx(Arg1, Arg2, Arg3, Arg4);
    }
    Arg1 = (Arg1) + (96);
    result = KeAcquireInStackQueuedSpinLock(Arg1, v_stack_m28, Arg3, Arg4);
    result = KeReleaseInStackQueuedSpinLock(v_stack_m28, v_stack_m28, Arg3, Arg4);
    local_rsp = (local_rsp) + (80);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x1A` | `8` | `R` |
| `Arg1` | `+ 0x1A` | `16` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0041F840&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0041F840[BB_0041F840]
  bb_0041F85E[BB_0041F85E]
  bb_0041F877[BB_0041F877]
  bb_0041F89A[BB_0041F89A]
  bb_0041F840 -->|branch| bb_0041F877
  bb_0041F840 -->|fallthrough| bb_0041F85E
  bb_0041F85E -->|flow| bb_0041F877
```
