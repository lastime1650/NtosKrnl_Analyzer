# SymCryptSha1Append

- RVA: `0x00528C70`–`0x00528C8F` (길이 `31` bytes)
- VA: `0x0000000140528C70`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005C788`
- 디코드: `9`개 명령, `31/31` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00528C84` → [SymCryptHashAppendInternal](SymCryptHashAppendInternal_function_0052D1FC.md) (function, `0x0052D1FC`)

### Direct callers
- [HashpHashBytes](../../page/84/HashpHashBytes_function_00841FA0.md) at `0x00841FF9`

### Static image references
- `0x00528C7D` → RVA `0x00006C00` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00528C70  48 83 EC 28                     sub rsp, 0x28
00528C74  4D 8B C8                        mov r9, r8
00528C77  4C 8B C2                        mov r8, rdx
00528C7A  48 8B D1                        mov rdx, rcx
00528C7D  48 8D 0D 7C DF AD FF            lea rcx, [rip - 0x522084]
00528C84  E8 73 45 00 00                  call 0x14052d1fc
00528C89  48 83 C4 28                     add rsp, 0x28
00528C8D  C3                              ret
00528C8E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptSha1Append(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = SymCryptHashAppendInternal(v_rip - 5382276, a1, a2, a3);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptSha1Append(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = SymCryptHashAppendInternal(v_rip - 5382276, Arg1, Arg2, Arg3);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00528C70&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00528C70[BB_00528C70]
  bb_00528C8E[BB_00528C8E]
```
