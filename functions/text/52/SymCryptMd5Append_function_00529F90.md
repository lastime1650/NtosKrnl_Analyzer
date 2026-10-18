# SymCryptMd5Append

- RVA: `0x00529F90`–`0x00529FAF` (길이 `31` bytes)
- VA: `0x0000000140529F90`
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
- `0x00529FA4` → [SymCryptHashAppendInternal](SymCryptHashAppendInternal_function_0052D1FC.md) (function, `0x0052D1FC`)

### Direct callers
- [HashpHashBytes](../../page/84/HashpHashBytes_function_00841FA0.md) at `0x00842007`

### Static image references
- `0x00529F9D` → RVA `0x00006C40` (`.rdata`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00529F90  48 83 EC 28                     sub rsp, 0x28
00529F94  4D 8B C8                        mov r9, r8
00529F97  4C 8B C2                        mov r8, rdx
00529F9A  48 8B D1                        mov rdx, rcx
00529F9D  48 8D 0D 9C CC AD FF            lea rcx, [rip - 0x523364]
00529FA4  E8 53 32 00 00                  call 0x14052d1fc
00529FA9  48 83 C4 28                     add rsp, 0x28
00529FAD  C3                              ret
00529FAE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall SymCryptMd5Append(__int64 a1, __int64 a2, __int64 a3)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (40);
    result = SymCryptHashAppendInternal(v_rip - 5387108, a1, a2, a3);
    v_rsp = (v_rsp) + (40);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t SymCryptMd5Append(int64_t Arg1, int64_t Arg2, int64_t Arg3)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (40);
    result = SymCryptHashAppendInternal(v_rip - 5387108, Arg1, Arg2, Arg3);
    local_rsp = (local_rsp) + (40);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00529F90&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00529F90[BB_00529F90]
  bb_00529FAE[BB_00529FAE]
```
