# sub_003E5FE3

- RVA: `0x003E5FE3`–`0x003E6023` (길이 `64` bytes)
- VA: `0x00000001403E5FE3`
- 실행 섹션: `.text`
- PDB 이름 있음: `아니요`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00094FBC`
- 디코드: `15`개 명령, `64/64` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x003E5FE6` → [memcmp](../6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)
- `0x003E6009` → [memcmp](../6C/memcmp_function_006C6B10.md) (function, `0x006C6B10`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- call이 아닌 외부 분기/꼬리 이동: **4**
  - `0x003E5FED` → [sub_003E5D8A + 0x14D](Unknown_function_003E5D8A.md) (`tail-transfer`)
  - `0x003E5FFE` → [sub_003E5D8A + 0x10E](Unknown_function_003E5D8A.md) (`tail-transfer`)
  - `0x003E6010` → [sub_003E5D8A + 0x116](Unknown_function_003E5D8A.md) (`tail-transfer`)
  - `0x003E6021` → [sub_003E5D8A + 0x23C](Unknown_function_003E5D8A.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
003E5FE3  48 8B CE                        mov rcx, rsi
003E5FE6  E8 25 0B 2E 00                  call 0x1406c6b10
003E5FEB  85 C0                           test eax, eax
003E5FED  0F 84 E4 FE FF FF               je 0x1403e5ed7
003E5FF3  44 8B 44 24 60                  mov r8d, dword ptr [rsp + 0x60]
003E5FF8  44 0F B7 4C 24 70               movzx r9d, word ptr [rsp + 0x70]
003E5FFE  E9 95 FE FF FF                  jmp 0x1403e5e98
003E6003  45 8B C1                        mov r8d, r9d
003E6006  48 8B CE                        mov rcx, rsi
003E6009  E8 02 0B 2E 00                  call 0x1406c6b10
003E600E  85 C0                           test eax, eax
003E6010  0F 84 8A FE FF FF               je 0x1403e5ea0
003E6016  44 0F B7 44 24 70               movzx r8d, word ptr [rsp + 0x70]
003E601C  44 8B 4C 24 60                  mov r9d, dword ptr [rsp + 0x60]
003E6021  EB A3                           jmp 0x1403e5fc6
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall sub_003E5FE3(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8, __int64 a9, __int64 a10, __int64 a11, unsigned int a12, __int64 a13, unsigned __int16 a14)
{
    __int64 result;
    unsigned int v_stack_p60;
    unsigned __int16 v_stack_p70;

    result = memcmp(v_rsi, a2, a3, a4);
}
```

## 5. (Beta) C Style

```c
int64_t sub_003E5FE3(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, uint64_t Arg5, uint64_t Arg6, uint64_t Arg7, uint64_t Arg8, uint64_t Arg9, uint64_t Arg10, uint64_t Arg11, uint32_t Arg12, uint64_t Arg13, uint16_t Arg14)
{
    int64_t result;
    uint32_t v_stack_p60;
    uint16_t v_stack_p70;

    result = memcmp(local_rsi, Arg2, Arg3, Arg4);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x003E5FE3&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_003E5FE3[BB_003E5FE3]
  bb_003E5FF3[BB_003E5FF3]
  bb_003E6003[BB_003E6003]
  bb_003E6016[BB_003E6016]
  bb_003E5FE3 -->|fallthrough| bb_003E5FF3
  bb_003E6003 -->|fallthrough| bb_003E6016
```
