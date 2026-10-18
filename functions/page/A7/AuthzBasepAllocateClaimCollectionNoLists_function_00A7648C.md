# AuthzBasepAllocateClaimCollectionNoLists

- RVA: `0x00A7648C`–`0x00A764C4` (길이 `56` bytes)
- VA: `0x0000000140A7648C`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005CF00`
- 디코드: `17`개 명령, `56/56` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00A7649D` → [AuthzBasepMemAlloc](../../text/2F/AuthzBasepMemAlloc_function_002FFD90.md) (function, `0x002FFD90`)
- `0x00A764B5` → [memset](../../text/6C/memset_function_006C6C40.md) (function, `0x006C6C40`)

### Direct callers
- [SepSetUserClaimAttributesToken](../7A/SepSetUserClaimAttributesToken_function_007A36C0.md) at `0x007A36ED`
- [SepCreateClaimAttributes](../A6/SepCreateClaimAttributes_function_00A6E154.md) at `0x00A6E1D8`
- [SepDuplicateClaimAttributes](SepDuplicateClaimAttributes_function_00A76334.md) at `0x00A7637E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x00A7649D` → [AuthzBasepMemAlloc](../../text/2F/AuthzBasepMemAlloc_function_002FFD90.md) (`PAGE` → `.text`)
  - `0x00A764B5` → [memset](../../text/6C/memset_function_006C6C40.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00A7648C  40 53                           push rbx
00A7648E  48 83 EC 20                     sub rsp, 0x20
00A76492  B9 60 02 00 00                  mov ecx, 0x260
00A76497  41 B8 53 65 41 74               mov r8d, 0x74416553
00A7649D  E8 EE 98 88 FF                  call 0x1402ffd90
00A764A2  48 8B D8                        mov rbx, rax
00A764A5  48 85 C0                        test rax, rax
00A764A8  74 13                           je 0x140a764bd
00A764AA  33 D2                           xor edx, edx
00A764AC  41 B8 60 02 00 00               mov r8d, 0x260
00A764B2  48 8B CB                        mov rcx, rbx
00A764B5  E8 86 07 C5 FF                  call 0x1406c6c40
00A764BA  48 8B C3                        mov rax, rbx
00A764BD  48 83 C4 20                     add rsp, 0x20
00A764C1  5B                              pop rbx
00A764C2  C3                              ret
00A764C3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall AuthzBasepAllocateClaimCollectionNoLists(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;

    v_rsp = (v_rsp) - (32);
    result = AuthzBasepMemAlloc(608, a2, (unsigned int)(0x74416553ULL), a4);
    if (result != 0) {
        a2 = 0;
        a3 = 608;
        a1 = result;
        result = memset(a1, a2, a3, a4);
        result = result;
    }
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t AuthzBasepAllocateClaimCollectionNoLists(int64_t Arg1, int32_t Arg2)
{
    int64_t result;
    int64_t local_rsp;

    local_rsp = (local_rsp) - (32);
    result = AuthzBasepMemAlloc(608, Arg2, (uint32_t)(0x74416553ULL), a4);
    if (result != 0) {
        Arg2 = 0;
        a3 = 608;
        Arg1 = result;
        result = memset(Arg1, Arg2, a3, a4);
        result = result;
    }
    local_rsp = (local_rsp) + (32);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A7648C&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00A7648C[BB_00A7648C]
  bb_00A764AA[BB_00A764AA]
  bb_00A764BD[BB_00A764BD]
  bb_00A764C3[BB_00A764C3]
  bb_00A7648C -->|branch| bb_00A764BD
  bb_00A7648C -->|fallthrough| bb_00A764AA
  bb_00A764AA -->|flow| bb_00A764BD
```
