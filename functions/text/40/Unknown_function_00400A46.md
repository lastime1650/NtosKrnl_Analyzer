# sub_00400A46

- RVA: `0x00400A46`–`0x00400A7A` (길이 `52` bytes)
- VA: `0x0000000140400A46`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009A29C`
- 디코드: `10`개 명령, `52/52` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00400A53` → [ObReleaseObjectSecurity](../../page/9D/ObReleaseObjectSecurity_function_009D77F0.md) (function, `0x009D77F0`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00400A53` → [ObReleaseObjectSecurity](../../page/9D/ObReleaseObjectSecurity_function_009D77F0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00400A46  48 85 FF                        test rdi, rdi
00400A49  74 0D                           je 0x140400a58
00400A4B  0F B6 54 24 30                  movzx edx, byte ptr [rsp + 0x30]
00400A50  48 8B CF                        mov rcx, rdi
00400A53  E8 98 6D 5D 00                  call 0x1409d77f0
00400A58  8B C3                           mov eax, ebx
00400A5A  4C 8B A4 24 C8 00 00 00         mov r12, qword ptr [rsp + 0xc8]
00400A62  48 8B BC 24 C0 00 00 00         mov rdi, qword ptr [rsp + 0xc0]
00400A6A  4C 8B AC 24 88 00 00 00         mov r13, qword ptr [rsp + 0x88]
00400A72  4C 8B BC 24 80 00 00 00         mov r15, qword ptr [rsp + 0x80]
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00400A46(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, unsigned __int8 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14, __int64 a15, __int64 a16, __int64 a17, __int64 a18, __int64 a19, __int64 a20, __int64 a21, __int64 a22, __int64 a23, __int64 a24, __int64 a25)
{
    __int64 result;

    if (v_rdi != 0) {
        a2 = a6;
        a1 = v_rdi;
        result = ObReleaseObjectSecurity(a1, a2, a3, a4);
    }
    return (unsigned int)((unsigned int)(v_rbx));
}
```

## 5. (Beta) C Style

```c
int64_t sub_00400A46(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint8_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, uint64_t Arg14, uint64_t Arg15, int64_t Arg16, int64_t Arg17, uint64_t Arg18, uint64_t Arg19, uint64_t Arg20, uint64_t Arg21, uint64_t Arg22, uint64_t Arg23, int64_t Arg24, int64_t Arg25)
{
    int64_t result;

    if (local_rdi != 0) {
        Arg2 = Arg6;
        Arg1 = local_rdi;
        result = ObReleaseObjectSecurity(Arg1, Arg2, Arg3, Arg4);
    }
    return (uint32_t)((uint32_t)(local_rbx));
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00400A46&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00400A46[BB_00400A46]
  bb_00400A4B[BB_00400A4B]
  bb_00400A58[BB_00400A58]
  bb_00400A46 -->|branch| bb_00400A58
  bb_00400A46 -->|fallthrough| bb_00400A4B
  bb_00400A4B -->|flow| bb_00400A58
```
