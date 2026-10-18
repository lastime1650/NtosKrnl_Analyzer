# sub_00B176D6

- RVA: `0x00B176D6`–`0x00B17700` (길이 `42` bytes)
- VA: `0x0000000140B176D6`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0006C3A0`
- 디코드: `12`개 명령, `42/42` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x00B176E1` → [CmpAssignKeySecurity](../7E/CmpAssignKeySecurity_function_007EC8B0.md) (function, `0x007EC8B0`)
- `0x00B176F5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00B176F5` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00B176EA` → [CmpSecurityMethod + 0x323](../87/CmpSecurityMethod_function_00870CC0.md) (`tail-transfer`)
  - `0x00B176FB` → [CmpSecurityMethod + 0x45F](../87/CmpSecurityMethod_function_00870CC0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00B176D6  48 8B 5C 24 58                  mov rbx, qword ptr [rsp + 0x58]
00B176DB  49 8B CD                        mov rcx, r13
00B176DE  48 8B D3                        mov rdx, rbx
00B176E1  E8 CA 51 CD FF                  call 0x1407ec8b0
00B176E6  8B F0                           mov esi, eax
00B176E8  85 C0                           test eax, eax
00B176EA  0F 88 F3 98 D5 FF               js 0x140870fe3
00B176F0  33 D2                           xor edx, edx
00B176F2  48 8B CB                        mov rcx, rbx
00B176F5  E8 76 B1 06 00                  call 0x140b82870
00B176FA  90                              nop
00B176FB  E9 1F 9A D5 FF                  jmp 0x14087111f
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_00B176D6(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11)
{
    __int64 result;

    result = CmpAssignKeySecurity(v_r13, a11, a3, a4);
    a2 = 0;
    result = ExFreePoolWithTag(a11, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_00B176D6(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, int64_t Arg11)
{
    int64_t result;

    result = CmpAssignKeySecurity(local_r13, Arg11, Arg3, Arg4);
    Arg2 = 0;
    result = ExFreePoolWithTag(Arg11, Arg2, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00B176D6&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00B176D6[BB_00B176D6]
  bb_00B176F0[BB_00B176F0]
  bb_00B176D6 -->|fallthrough| bb_00B176F0
```
