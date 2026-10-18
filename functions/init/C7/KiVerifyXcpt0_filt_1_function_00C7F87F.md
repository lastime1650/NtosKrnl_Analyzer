# KiVerifyXcpt0$filt$1

- RVA: `0x00C7F87F`–`0x00C7F8A9` (길이 `42` bytes)
- VA: `0x0000000140C7F87F`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF6EC`
- 디코드: `16`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00C7F899` → [KiVerifyXcptFilter](../C3/KiVerifyXcptFilter_function_00C3ADD0.md) (function, `0x00C3ADD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C7F87F  40 55                           push rbp
00C7F881  48 83 EC 20                     sub rsp, 0x20
00C7F885  48 8B EA                        mov rbp, rdx
00C7F888  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00C7F88C  8B 41 0C                        mov eax, dword ptr [rcx + 0xc]
00C7F88F  FF C0                           inc eax
00C7F891  89 41 0C                        mov dword ptr [rcx + 0xc], eax
00C7F894  83 F8 01                        cmp eax, 1
00C7F897  75 07                           jne 0x140c7f8a0
00C7F899  E8 32 B5 FB FF                  call 0x140c3add0
00C7F89E  EB 02                           jmp 0x140c7f8a2
00C7F8A0  33 C0                           xor eax, eax
00C7F8A2  48 83 C4 20                     add rsp, 0x20
00C7F8A6  5D                              pop rbp
00C7F8A7  C3                              ret
00C7F8A8  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiVerifyXcpt0_filt_1(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 48) + 12))) + 1);
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 48) + 12) = (unsigned int)(result);
    if (((unsigned int)(result)) != 1) goto loc_00C7F8A0;
    result = KiVerifyXcptFilter(*(unsigned __int64 *)(a2 + 48), a2, a3, a4);
    goto loc_00C7F8A2;
loc_00C7F8A0:
    result = 0;
loc_00C7F8A2:
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiVerifyXcpt0_filt_1(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x30) + 0xC))) + 1);
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x30) + 0xC) = (uint32_t)(result);
    if (((uint32_t)(result)) != 1) goto loc_00C7F8A0;
    result = KiVerifyXcptFilter(*(uint64_t *)(arg2 + 0x30), Arg2, a3, a4);
    goto loc_00C7F8A2;
loc_00C7F8A0:
    result = 0;
loc_00C7F8A2:
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x30` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C7F87F&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C7F87F[BB_00C7F87F]
  bb_00C7F899[BB_00C7F899]
  bb_00C7F8A0[BB_00C7F8A0]
  bb_00C7F8A2[BB_00C7F8A2]
  bb_00C7F8A8[BB_00C7F8A8]
  bb_00C7F87F -->|branch| bb_00C7F8A0
  bb_00C7F87F -->|fallthrough| bb_00C7F899
  bb_00C7F899 -->|branch| bb_00C7F8A2
  bb_00C7F8A0 -->|flow| bb_00C7F8A2
```
