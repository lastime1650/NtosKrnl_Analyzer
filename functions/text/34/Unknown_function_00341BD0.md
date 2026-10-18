# sub_00341BD0

- RVA: `0x00341BD0`–`0x00341BF0` (길이 `32` bytes)
- VA: `0x0000000140341BD0`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00077640`
- 디코드: `8`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **2**
  - `0x00341BDC` → [sub_00341C71](Unknown_function_00341C71.md) (`tail-transfer`)
  - `0x00341BEE` → [sub_00341BF0 + 0x1B](Unknown_function_00341BF0.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00341BD0  48 8D 54 24 30                  lea rdx, [rsp + 0x30]
00341BD5  48 87 55 00                     xchg qword ptr [rbp], rdx
00341BD9  48 85 D2                        test rdx, rdx
00341BDC  0F 85 8F 00 00 00               jne 0x140341c71
00341BE2  48 8B 4B 10                     mov rcx, qword ptr [rbx + 0x10]
00341BE6  48 8B 6C 24 70                  mov rbp, qword ptr [rsp + 0x70]
00341BEB  48 85 C9                        test rcx, rcx
00341BEE  74 1B                           je 0x140341c0b
```

## 4. C-style interpretation (structured pseudocode)

```c
void __fastcall sub_00341BD0(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, __int64 a12, __int64 a13, __int64 a14)
{
}
```

## 5. (Beta) C Style

```c
void sub_00341BD0(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, int64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint64_t Arg12, uint64_t Arg13, int64_t Arg14)
{
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00341BD0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00341BD0[BB_00341BD0]
  bb_00341BE2[BB_00341BE2]
  bb_00341BD0 -->|fallthrough| bb_00341BE2
```
