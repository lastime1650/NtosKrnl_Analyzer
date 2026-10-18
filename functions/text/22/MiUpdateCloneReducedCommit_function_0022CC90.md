# MiUpdateCloneReducedCommit

- RVA: `0x0022CC90`–`0x0022CCF9` (길이 `105` bytes)
- VA: `0x000000014022CC90`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000DB714`
- 디코드: `28`개 명령, `105/105` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- [MiDecrementCloneBlock](MiDecrementCloneBlock_function_0022BA8C.md) at `0x0022BBAF`
- [MiWriteSharedDemandZeroPte](../4A/MiWriteSharedDemandZeroPte_function_004A8DDC.md) at `0x004A8E20`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0022CC90  4C 8B 41 10                     mov r8, qword ptr [rcx + 0x10]
0022CC94  4C 8B C9                        mov r9, rcx
0022CC97  85 D2                           test edx, edx
0022CC99  75 3B                           jne 0x14022ccd6
0022CC9B  49 8B C8                        mov rcx, r8
0022CC9E  48 C1 E9 05                     shr rcx, 5
0022CCA2  48 FF C9                        dec rcx
0022CCA5  48 C1 E1 05                     shl rcx, 5
0022CCA9  48 8B C1                        mov rax, rcx
0022CCAC  49 33 C0                        xor rax, r8
0022CCAF  49 B8 1F 00 00 00 00 00 00 F0   movabs r8, 0xf00000000000001f
0022CCB9  49 23 C0                        and rax, r8
0022CCBC  48 33 C1                        xor rax, rcx
0022CCBF  49 89 41 10                     mov qword ptr [r9 + 0x10], rax
0022CCC3  48 B9 FF FF FF FF FF FF 7F 00   movabs rcx, 0x7fffffffffffff
0022CCCD  48 C1 E8 05                     shr rax, 5
0022CCD1  48 23 C1                        and rax, rcx
0022CCD4  C3                              ret
0022CCD5  CC                              int3
0022CCD6  49 8B D0                        mov rdx, r8
0022CCD9  48 83 E2 E0                     and rdx, 0xffffffffffffffe0
0022CCDD  48 83 C2 20                     add rdx, 0x20
0022CCE1  48 8B C2                        mov rax, rdx
0022CCE4  49 33 C0                        xor rax, r8
0022CCE7  49 B8 1F 00 00 00 00 00 00 F0   movabs r8, 0xf00000000000001f
0022CCF1  49 23 C0                        and rax, r8
0022CCF4  48 33 C2                        xor rax, rdx
0022CCF7  EB C6                           jmp 0x14022ccbf
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiUpdateCloneReducedCommit(__int64 a1, int a2)
{
    __int64 result;

    if (a2 != 0) goto loc_0022CCD6;
    a1 = (*(unsigned __int64 *)(a1 + 16)) >> (5);
    a1 = (a1) - 1;
    a1 = (a1) << (5);
    result = (a1) ^ (*(unsigned __int64 *)(a1 + 16));
    result = (result) & (*(unsigned __int64 *)(a1 + 16));
    result = (result) ^ (a1);
loc_0022CCBF:
    *(unsigned __int64 *)(a1 + 16) = result;
    result = (result) >> (5);
    result = (result) & (a1);
    return result;
loc_0022CCD6:
    a2 = (*(unsigned __int64 *)(a1 + 16)) & (-32);
    a2 = (a2) + (32);
    result = (a2) ^ (*(unsigned __int64 *)(a1 + 16));
    result = (result) & (*(unsigned __int64 *)(a1 + 16));
    result = (result) ^ (a2);
    goto loc_0022CCBF;
}
```

## 5. (Beta) C Style

```c
int64_t MiUpdateCloneReducedCommit(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;

    if (Arg2 != 0) goto loc_0022CCD6;
    Arg1 = (*(uint64_t *)(arg1 + 0x10)) >> (5);
    Arg1 = (Arg1) - 1;
    Arg1 = (Arg1) << (5);
    result = (Arg1) ^ (*(uint64_t *)(arg1 + 0x10));
    result = (result) & (*(uint64_t *)(arg1 + 0x10));
    result = (result) ^ (Arg1);
loc_0022CCBF:
    *(uint64_t *)(arg1 + 0x10) = result;
    result = (result) >> (5);
    result = (result) & (Arg1);
    return result;
loc_0022CCD6:
    Arg2 = (*(uint64_t *)(arg1 + 0x10)) & (-32);
    Arg2 = (Arg2) + (32);
    result = (Arg2) ^ (*(uint64_t *)(arg1 + 0x10));
    result = (result) & (*(uint64_t *)(arg1 + 0x10));
    result = (result) ^ (Arg2);
    goto loc_0022CCBF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0022CC90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0022CC90[BB_0022CC90]
  bb_0022CC9B[BB_0022CC9B]
  bb_0022CCBF[BB_0022CCBF]
  bb_0022CCD5[BB_0022CCD5]
  bb_0022CCD6[BB_0022CCD6]
  bb_0022CC90 -->|branch| bb_0022CCD6
  bb_0022CC90 -->|fallthrough| bb_0022CC9B
  bb_0022CC9B -->|flow| bb_0022CCBF
  bb_0022CCD5 -->|flow| bb_0022CCD6
  bb_0022CCD6 -->|branch| bb_0022CCBF
```
