# SepSinglePrivilegeCheck

- RVA: `0x003D191C`–`0x003D1963` (길이 `71` bytes)
- VA: `0x00000001403D191C`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000911B0`
- 디코드: `21`개 명령, `71/71` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **4**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [SepAccessCheckEx](../3C/SepAccessCheckEx_function_003CF7B0.md) at `0x003CFB7C`
- [SepAccessCheckEx](../3C/SepAccessCheckEx_function_003CF7B0.md) at `0x003CFC6D`
- [SepAccessCheck](SepAccessCheck_function_003D0E54.md) at `0x003D12AC`
- [SepAccessCheck](SepAccessCheck_function_003D0E54.md) at `0x003D1359`
- [SepAccessCheck](SepAccessCheck_function_003D0E54.md) at `0x003D139B`
- [SePrivilegePolicyCheck](SePrivilegePolicyCheck_function_003D1700.md) at `0x003D17EA`
- [SePrivilegePolicyCheck](SePrivilegePolicyCheck_function_003D1700.md) at `0x003D1806`
- [sub_006E89DA](../6E/Unknown_function_006E89DA.md) at `0x006E8A6E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
003D191C  48 83 EC 18                     sub rsp, 0x18
003D1920  45 33 C9                        xor r9d, r9d
003D1923  4C 89 4C 24 08                  mov qword ptr [rsp + 8], r9
003D1928  4C 89 0C 24                     mov qword ptr [rsp], r9
003D192C  45 84 C0                        test r8b, r8b
003D192F  74 2E                           je 0x1403d195f
003D1931  48 8B 42 48                     mov rax, qword ptr [rdx + 0x48]
003D1935  48 87 44 24 08                  xchg qword ptr [rsp + 8], rax
003D193A  48 8B 52 40                     mov rdx, qword ptr [rdx + 0x40]
003D193E  48 87 14 24                     xchg qword ptr [rsp], rdx
003D1942  4C 8B 04 24                     mov r8, qword ptr [rsp]
003D1946  4C 23 44 24 08                  and r8, qword ptr [rsp + 8]
003D194B  F0 44 09 0C 24                  lock or dword ptr [rsp], r9d
003D1950  8B C1                           mov eax, ecx
003D1952  49 0F A3 C0                     bt r8, rax
003D1956  0F 92 C0                        setb al
003D1959  48 83 C4 18                     add rsp, 0x18
003D195D  C3                              ret
003D195E  CC                              int3
003D195F  B0 01                           mov al, 1
003D1961  EB F6                           jmp 0x1403d1959
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SepSinglePrivilegeCheck(int a1, __int64 a2, unsigned __int8 a3, int a4)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (24);
    a4 = 0;
    v_stack_m10 = 0;
    v_stack_m18 = 0;
    if (a3 == 0) goto loc_003D195F;
    a3 = (v_stack_m18) & (v_stack_m10);
    result = (condition_is_below) ? 1 : 0;
loc_003D1959:
    v_rsp = (v_rsp) + (24);
    return result;
loc_003D195F:
    goto loc_003D1959;
}
```

## 5. (Beta) C Style

```c
int64_t SepSinglePrivilegeCheck(int32_t Arg1, void *Arg2, uint8_t Arg3, int32_t Arg4)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (24);
    Arg4 = 0;
    v_stack_m10 = 0;
    v_stack_m18 = 0;
    if (Arg3 == 0) goto loc_003D195F;
    Arg3 = (v_stack_m18) & (v_stack_m10);
    result = (condition_is_below) ? 1 : 0;
loc_003D1959:
    local_rsp = (local_rsp) + (24);
    return result;
loc_003D195F:
    goto loc_003D1959;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x48` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003D191C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003D191C[BB_003D191C]
  bb_003D1931[BB_003D1931]
  bb_003D1959[BB_003D1959]
  bb_003D195E[BB_003D195E]
  bb_003D195F[BB_003D195F]
  bb_003D191C -->|branch| bb_003D195F
  bb_003D191C -->|fallthrough| bb_003D1931
  bb_003D1931 -->|flow| bb_003D1959
  bb_003D195E -->|flow| bb_003D195F
  bb_003D195F -->|branch| bb_003D1959
```
