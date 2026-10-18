# KiVerifyXcpt10$fin$8

- RVA: `0x00C7FAA1`–`0x00C7FAEB` (길이 `74` bytes)
- VA: `0x0000000140C7FAA1`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF6EC`
- 디코드: `25`개 명령, `74/74` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00C7FACE` → [KiVerifyXcptFilter](../C3/KiVerifyXcptFilter_function_00C3ADD0.md) (function, `0x00C3ADD0`)
- `0x00C7FADE` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (function, `0x004FFB40`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00C7FAD3` → RVA `0x00C3A940` (`INIT`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00C7FADE` → [local_unwind](../../text/4F/local_unwind_function_004FFB40.md) (`INIT` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C7FAA1  40 55                           push rbp
00C7FAA3  48 83 EC 20                     sub rsp, 0x20
00C7FAA7  48 8B EA                        mov rbp, rdx
00C7FAAA  48 8B 6D 38                     mov rbp, qword ptr [rbp + 0x38]
00C7FAAE  48 8B 55 40                     mov rdx, qword ptr [rbp + 0x40]
00C7FAB2  8B 42 0C                        mov eax, dword ptr [rdx + 0xc]
00C7FAB5  83 C0 0B                        add eax, 0xb
00C7FAB8  89 42 0C                        mov dword ptr [rdx + 0xc], eax
00C7FABB  83 F8 63                        cmp eax, 0x63
00C7FABE  75 0B                           jne 0x140c7facb
00C7FAC0  48 8B 02                        mov rax, qword ptr [rdx]
00C7FAC3  8B 08                           mov ecx, dword ptr [rax]
00C7FAC5  FF C1                           inc ecx
00C7FAC7  89 08                           mov dword ptr [rax], ecx
00C7FAC9  EB 19                           jmp 0x140c7fae4
00C7FACB  48 8B CA                        mov rcx, rdx
00C7FACE  E8 FD B2 FB FF                  call 0x140c3add0
00C7FAD3  48 8D 15 66 AE FB FF            lea rdx, [rip - 0x4519a]
00C7FADA  48 8B 4D 20                     mov rcx, qword ptr [rbp + 0x20]
00C7FADE  E8 5D 00 88 FF                  call 0x1404ffb40
00C7FAE3  90                              nop
00C7FAE4  48 83 C4 20                     add rsp, 0x20
00C7FAE8  5D                              pop rbp
00C7FAE9  C3                              ret
00C7FAEA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiVerifyXcpt10_fin_8(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 56) + 64) + 12))) + (11));
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 56) + 64) + 12) = (unsigned int)(result);
    if (((unsigned int)(result)) != 99) goto loc_00C7FACB;
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 56) + 64))))) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 56) + 64))) = (unsigned int)(a1);
    goto loc_00C7FAE4;
loc_00C7FACB:
    result = KiVerifyXcptFilter(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 56) + 64), *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 56) + 64), a3, a4);
    result = local_unwind(*(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 56) + 32), v_rip - 283034, a3, a4);
loc_00C7FAE4:
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiVerifyXcpt10_fin_8(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x38) + 0x40) + 0xC))) + (11));
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x38) + 0x40) + 0xC) = (uint32_t)(result);
    if (((uint32_t)(result)) != 99) goto loc_00C7FACB;
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x38) + 0x40))))) + 1);
    *(uint32_t *)(*(uint64_t *)(*(uint64_t *)(*(uint64_t *)(arg2 + 0x38) + 0x40))) = (uint32_t)(Arg1);
    goto loc_00C7FAE4;
loc_00C7FACB:
    result = KiVerifyXcptFilter(*(uint64_t *)(*(uint64_t *)(arg2 + 0x38) + 0x40), *(uint64_t *)(*(uint64_t *)(arg2 + 0x38) + 0x40), a3, a4);
    result = local_unwind(*(uint64_t *)(*(uint64_t *)(arg2 + 0x38) + 0x20), v_rip - 283034, a3, a4);
loc_00C7FAE4:
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x38` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C7FAA1&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C7FAA1[BB_00C7FAA1]
  bb_00C7FAC0[BB_00C7FAC0]
  bb_00C7FACB[BB_00C7FACB]
  bb_00C7FAE4[BB_00C7FAE4]
  bb_00C7FAEA[BB_00C7FAEA]
  bb_00C7FAA1 -->|branch| bb_00C7FACB
  bb_00C7FAA1 -->|fallthrough| bb_00C7FAC0
  bb_00C7FAC0 -->|branch| bb_00C7FAE4
  bb_00C7FACB -->|flow| bb_00C7FAE4
```
