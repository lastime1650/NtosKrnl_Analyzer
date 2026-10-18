# PiSwDeviceCreate

- RVA: `0x008DB8EC`–`0x008DB94F` (길이 `99` bytes)
- VA: `0x00000001408DB8EC`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006CF28`
- 디코드: `29`개 명령, `99/99` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x008DB909` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (function, `0x00B820F0`)

### Direct callers
- [PiSwIrpStartCreateWorker](PiSwIrpStartCreateWorker_function_008DB398.md) at `0x008DB406`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x008DB909` → [ExAllocatePool2](../../poolcode/B8/ExAllocatePool2_function_00B820F0.md) (`PAGE` → `POOLCODE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
008DB8EC  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
008DB8F1  57                              push rdi
008DB8F2  48 83 EC 20                     sub rsp, 0x20
008DB8F6  BA D0 00 00 00                  mov edx, 0xd0
008DB8FB  48 8B F9                        mov rdi, rcx
008DB8FE  41 B8 50 6E 70 57               mov r8d, 0x57706e50
008DB904  33 DB                           xor ebx, ebx
008DB906  8D 4A 30                        lea ecx, [rdx + 0x30]
008DB909  E8 E2 67 2A 00                  call 0x140b820f0
008DB90E  48 89 07                        mov qword ptr [rdi], rax
008DB911  48 85 C0                        test rax, rax
008DB914  74 32                           je 0x1408db948
008DB916  C7 00 01 00 00 00               mov dword ptr [rax], 1
008DB91C  48 8B 07                        mov rax, qword ptr [rdi]
008DB91F  48 83 E8 80                     sub rax, -0x80
008DB923  48 89 40 08                     mov qword ptr [rax + 8], rax
008DB927  48 89 00                        mov qword ptr [rax], rax
008DB92A  48 8B 07                        mov rax, qword ptr [rdi]
008DB92D  48 05 B8 00 00 00               add rax, 0xb8
008DB933  48 89 40 08                     mov qword ptr [rax + 8], rax
008DB937  48 89 00                        mov qword ptr [rax], rax
008DB93A  8B C3                           mov eax, ebx
008DB93C  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
008DB941  48 83 C4 20                     add rsp, 0x20
008DB945  5F                              pop rdi
008DB946  C3                              ret
008DB947  CC                              int3
008DB948  BB 9A 00 00 C0                  mov ebx, 0xc000009a
008DB94D  EB EB                           jmp 0x1408db93a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiSwDeviceCreate(__int64 a1)
{
    __int64 result;
    __int64 v_rbx;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_rbx = 0;
    result = ExAllocatePool2(208 + 48, 208, (unsigned int)(0x57706E50ULL), a4);
    *(unsigned __int64 *)(a1) = result;
    if (result == 0) goto loc_008DB948;
    *(unsigned int *)(result) = 1;
    result = (*(unsigned __int64 *)(a1)) - (-128);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
    result = (*(unsigned __int64 *)(a1)) + (184);
    *(unsigned __int64 *)(result + 8) = result;
    *(unsigned __int64 *)(result) = result;
loc_008DB93A:
    v_rsp = (v_rsp) + (32);
    return 0;
loc_008DB948:
    goto loc_008DB93A;
}
```

## 5. (Beta) C Style

```c
int64_t PiSwDeviceCreate(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbx;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_rbx = 0;
    result = ExAllocatePool2(208 + 48, 208, (uint32_t)(0x57706E50ULL), a4);
    *(uint64_t *)(arg1) = result;
    if (result == 0) goto loc_008DB948;
    *(uint32_t *)(result) = 1;
    result = (*(uint64_t *)(arg1)) - (-128);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
    result = (*(uint64_t *)(arg1)) + (184);
    *(uint64_t *)(result + 0x8) = result;
    *(uint64_t *)(result) = result;
loc_008DB93A:
    local_rsp = (local_rsp) + (32);
    return 0;
loc_008DB948:
    goto loc_008DB93A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x0` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x008DB8EC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_008DB8EC[BB_008DB8EC]
  bb_008DB916[BB_008DB916]
  bb_008DB93A[BB_008DB93A]
  bb_008DB947[BB_008DB947]
  bb_008DB948[BB_008DB948]
  bb_008DB8EC -->|branch| bb_008DB948
  bb_008DB8EC -->|fallthrough| bb_008DB916
  bb_008DB916 -->|flow| bb_008DB93A
  bb_008DB947 -->|flow| bb_008DB948
  bb_008DB948 -->|branch| bb_008DB93A
```
