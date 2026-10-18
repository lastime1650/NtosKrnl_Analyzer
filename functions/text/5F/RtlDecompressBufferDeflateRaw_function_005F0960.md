# RtlDecompressBufferDeflateRaw

- RVA: `0x005F0960`–`0x005F0996` (길이 `54` bytes)
- VA: `0x00000001405F0960`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00063458`
- 디코드: `14`개 명령, `54/54` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005F098B` → [RtlDecompressBufferDeflateInternal](RtlDecompressBufferDeflateInternal_function_005F0858.md) (function, `0x005F0858`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005F0960  48 83 EC 48                     sub rsp, 0x48
005F0964  48 8B 84 24 80 00 00 00         mov rax, qword ptr [rsp + 0x80]
005F096C  48 89 44 24 38                  mov qword ptr [rsp + 0x38], rax
005F0971  48 8B 44 24 78                  mov rax, qword ptr [rsp + 0x78]
005F0976  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
005F097B  44 89 4C 24 20                  mov dword ptr [rsp + 0x20], r9d
005F0980  4D 8B C8                        mov r9, r8
005F0983  44 8B C2                        mov r8d, edx
005F0986  48 8B D1                        mov rdx, rcx
005F0989  33 C9                           xor ecx, ecx
005F098B  E8 C8 FE FF FF                  call 0x1405f0858
005F0990  48 83 C4 48                     add rsp, 0x48
005F0994  C3                              ret
005F0995  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlDecompressBufferDeflateRaw(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, __int64 a6, __int64 a7)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m10;
    unsigned __int64 v_stack_m18;
    unsigned int v_stack_m28;

    v_rsp = (v_rsp) - (72);
    v_stack_m10 = a7;
    v_stack_m18 = a6;
    v_stack_m28 = a4;
    a1 = 0;
    result = RtlDecompressBufferDeflateInternal(a1, a1, (unsigned int)(a2), a3);
    v_rsp = (v_rsp) + (72);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t RtlDecompressBufferDeflateRaw(int64_t Arg1, int32_t Arg2, int64_t Arg3, int32_t Arg4, uint64_t Arg5, int64_t Arg6, int64_t Arg7)
{
    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m10;
    uint64_t v_stack_m18;
    uint32_t v_stack_m28;

    local_rsp = (local_rsp) - (72);
    v_stack_m10 = Arg7;
    v_stack_m18 = Arg6;
    v_stack_m28 = Arg4;
    Arg1 = 0;
    result = RtlDecompressBufferDeflateInternal(Arg1, Arg1, (uint32_t)(Arg2), Arg3);
    local_rsp = (local_rsp) + (72);
    return result;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005F0960&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005F0960[BB_005F0960]
  bb_005F0995[BB_005F0995]
```
