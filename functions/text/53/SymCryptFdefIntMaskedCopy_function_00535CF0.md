# SymCryptFdefIntMaskedCopy

- RVA: `0x00535CF0`–`0x00535D0E` (길이 `30` bytes)
- VA: `0x0000000140535CF0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `30/30` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00535D03` → [SymCryptFdefMaskedCopyAsm](SymCryptFdefMaskedCopyAsm_function_005365D0.md) (function, `0x005365D0`)

### Direct callers
- [SymCryptIntMaskedCopy](../52/SymCryptIntMaskedCopy_function_005256E0.md) at `0x005256E4`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00535CF0  48 83 EC 28                     sub rsp, 0x28
00535CF4  45 8B C8                        mov r9d, r8d
00535CF7  48 83 C2 20                     add rdx, 0x20
00535CFB  44 8B 41 04                     mov r8d, dword ptr [rcx + 4]
00535CFF  48 83 C1 20                     add rcx, 0x20
00535D03  E8 C8 08 00 00                  call 0x1405365d0
00535D08  48 83 C4 28                     add rsp, 0x28
00535D0C  C3                              ret
00535D0D  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptFdefIntMaskedCopy(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    a2 = (a2) + (32);
    a1 = (a1) + (32);
    result = SymCryptFdefMaskedCopyAsm(a1, a2, (unsigned int)(*(unsigned int *)(a1 + 4)), (unsigned int)(a3));
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptFdefIntMaskedCopy(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    Arg2 = (Arg2) + (32);
    Arg1 = (Arg1) + (32);
    result = SymCryptFdefMaskedCopyAsm(Arg1, Arg2, (uint32_t)(*(uint32_t *)(arg1 + 0x4)), (uint32_t)(Arg3));
    local_rsp = (local_rsp) + (40);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00535CF0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00535CF0[BB_00535CF0]
  bb_00535D0D[BB_00535D0D]
```
