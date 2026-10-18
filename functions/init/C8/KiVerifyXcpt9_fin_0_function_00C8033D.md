# KiVerifyXcpt9$fin$0

- RVA: `0x00C8033D`–`0x00C80378` (길이 `59` bytes)
- VA: `0x0000000140C8033D`
- 실행 섹션: `INIT`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000BF6EC`
- 디코드: `21`개 명령, `59/59` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00C80363` → [KiVerifyXcptFilter](../C3/KiVerifyXcptFilter_function_00C3ADD0.md) (function, `0x00C3ADD0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00C8033D  40 55                           push rbp
00C8033F  48 83 EC 20                     sub rsp, 0x20
00C80343  48 8B EA                        mov rbp, rdx
00C80346  84 C9                           test cl, cl
00C80348  74 27                           je 0x140c80371
00C8034A  4C 8B 45 40                     mov r8, qword ptr [rbp + 0x40]
00C8034E  41 8B 40 0C                     mov eax, dword ptr [r8 + 0xc]
00C80352  83 C0 0A                        add eax, 0xa
00C80355  41 83 78 0C 0A                  cmp dword ptr [r8 + 0xc], 0xa
00C8035A  41 89 40 0C                     mov dword ptr [r8 + 0xc], eax
00C8035E  75 11                           jne 0x140c80371
00C80360  49 8B C8                        mov rcx, r8
00C80363  E8 68 AA FB FF                  call 0x140c3add0
00C80368  49 8B 10                        mov rdx, qword ptr [r8]
00C8036B  8B 0A                           mov ecx, dword ptr [rdx]
00C8036D  FF C1                           inc ecx
00C8036F  89 0A                           mov dword ptr [rdx], ecx
00C80371  48 83 C4 20                     add rsp, 0x20
00C80375  5D                              pop rbp
00C80376  C3                              ret
00C80377  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiVerifyXcpt9_fin_0(unsigned __int8 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    if (a1 == 0) goto loc_00C80371;
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 12))) + (10));
    *(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 12) = (unsigned int)(result);
    if ((*(unsigned int *)(*(unsigned __int64 *)(a2 + 64) + 12)) == 10) {
        a1 = *(unsigned __int64 *)(a2 + 64);
        result = KiVerifyXcptFilter(a1, a2, *(unsigned __int64 *)(a2 + 64), a4);
        a2 = *(unsigned __int64 *)(*(unsigned __int64 *)(a2 + 64));
        a1 = *(unsigned int *)(a2);
        a1 = (unsigned int)((a1) + 1);
        *(unsigned int *)(a2) = a1;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiVerifyXcpt9_fin_0(uint8_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    if (Arg1 == 0) goto loc_00C80371;
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0xC))) + (10));
    *(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0xC) = (uint32_t)(result);
    if ((*(uint32_t *)(*(uint64_t *)(arg2 + 0x40) + 0xC)) == 10) {
        Arg1 = *(uint64_t *)(arg2 + 0x40);
        result = KiVerifyXcptFilter(Arg1, Arg2, *(uint64_t *)(arg2 + 0x40), a4);
        Arg2 = *(uint64_t *)(*(uint64_t *)(arg2 + 0x40));
        Arg1 = *(uint32_t *)(arg2);
        Arg1 = (uint32_t)((Arg1) + 1);
        *(uint32_t *)(arg2) = Arg1;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x40` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=init&rva=0x00C8033D&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00C8033D[BB_00C8033D]
  bb_00C8034A[BB_00C8034A]
  bb_00C80360[BB_00C80360]
  bb_00C80371[BB_00C80371]
  bb_00C80377[BB_00C80377]
  bb_00C8033D -->|branch| bb_00C80371
  bb_00C8033D -->|fallthrough| bb_00C8034A
  bb_00C8034A -->|branch| bb_00C80371
  bb_00C8034A -->|fallthrough| bb_00C80360
  bb_00C80360 -->|flow| bb_00C80371
```
