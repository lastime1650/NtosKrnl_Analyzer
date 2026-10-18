# IopGetMountFlag

- RVA: `0x00272444`–`0x0027248F` (길이 `75` bytes)
- VA: `0x0000000140272444`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CAAC`
- 디코드: `23`개 명령, `75/75` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00272456` → [KeAcquireQueuedSpinLock](KeAcquireQueuedSpinLock_function_00273D80.md) (function, `0x00273D80`)
- `0x0027247B` → [KeReleaseQueuedSpinLock](KeReleaseQueuedSpinLock_function_00272540.md) (function, `0x00272540`)

### Direct callers
- [NtQueryVolumeInformationFile](../../page/8A/NtQueryVolumeInformationFile_function_008AC8C0.md) at `0x008ACD3F`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00272444  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00272449  57                              push rdi
0027244A  48 83 EC 20                     sub rsp, 0x20
0027244E  48 8B D9                        mov rbx, rcx
00272451  33 FF                           xor edi, edi
00272453  8D 4F 09                        lea ecx, [rdi + 9]
00272456  E8 25 19 00 00                  call 0x140273d80
0027245B  8A D0                           mov dl, al
0027245D  48 8B 43 38                     mov rax, qword ptr [rbx + 0x38]
00272461  48 85 C0                        test rax, rax
00272464  74 10                           je 0x140272476
00272466  44 8D 47 01                     lea r8d, [rdi + 1]
0027246A  40 0F B6 FF                     movzx edi, dil
0027246E  44 84 40 04                     test byte ptr [rax + 4], r8b
00272472  41 0F 45 F8                     cmovne edi, r8d
00272476  B9 09 00 00 00                  mov ecx, 9
0027247B  E8 C0 00 00 00                  call 0x140272540
00272480  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
00272485  40 8A C7                        mov al, dil
00272488  48 83 C4 20                     add rsp, 0x20
0027248C  5F                              pop rdi
0027248D  C3                              ret
0027248E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall IopGetMountFlag(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_rsp = (v_rsp) - (32);
    v_rdi = 0;
    result = KeAcquireQueuedSpinLock(v_rdi + 9, a2, a3, a4);
    if (*(unsigned __int64 *)(a1 + 56) != 0) {
        a3 = v_rdi + 1;
        v_rdi = 0;
        if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a1 + 56) + 4)) & ((unsigned __int8)(a3))) != 0) { v_rdi = (unsigned int)(a3); }
    }
    result = KeReleaseQueuedSpinLock(9, (unsigned __int8)(result), a3, a4);
    v_rsp = (v_rsp) + (32);
    return (unsigned __int8)(v_rdi);
}
```

## 5. (Beta) C Style

```c
int64_t IopGetMountFlag(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    local_rsp = (local_rsp) - (32);
    local_rdi = 0;
    result = KeAcquireQueuedSpinLock(local_rdi + 9, a2, a3, a4);
    if (*(uint64_t *)(arg1 + 0x38) != 0) {
        a3 = local_rdi + 1;
        local_rdi = 0;
        if (((*(uint8_t *)(*(uint64_t *)(arg1 + 0x38) + 0x4)) & ((uint8_t)(a3))) != 0) { local_rdi = (uint32_t)(a3); }
    }
    result = KeReleaseQueuedSpinLock(9, (uint8_t)(result), a3, a4);
    local_rsp = (local_rsp) + (32);
    return (uint8_t)(local_rdi);
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00272444&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00272444[BB_00272444]
  bb_00272466[BB_00272466]
  bb_00272476[BB_00272476]
  bb_0027248E[BB_0027248E]
  bb_00272444 -->|branch| bb_00272476
  bb_00272444 -->|fallthrough| bb_00272466
  bb_00272466 -->|flow| bb_00272476
```
